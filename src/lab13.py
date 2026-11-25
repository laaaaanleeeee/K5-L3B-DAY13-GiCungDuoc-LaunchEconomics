"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    # Lần chạy thứ i chỉ xảy ra khi i-1 lần trước đều sai: P = (1-p)^(i-1).
    # Cộng i = 1..k → (1 - (1-p)^k) / p ; k → ∞ → 1/p (phân phối hình học).
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    # = số lần chạy trung bình ÷ tỉ lệ thành công; (1-(1-p)^k) triệt tiêu → luôn = 1/p.
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    # Chỉ giữ các lần chạy thuộc tập yêu cầu đang xét (để A3 lọc theo loai là đủ).
    runs = runs[runs['request_id'].isin(reqs['request_id'])]

    if max_lan_chay is not None:  # Nhiệm vụ B: giới hạn số lần chạy
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    # Tử số: MỌI lần chạy, kể cả lần lỗi (lần lỗi vẫn tốn token và tool).
    tien_moi_lan = (runs['tokens_in'] / 1000 * gia_vao
                    + runs['tokens_out'] / 1000 * gia_ra
                    + runs['tool_calls'] * gia_tool)
    token = (runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra).sum()
    tool = (runs['tool_calls'] * gia_tool).sum()
    chay_lai = tien_moi_lan[runs['attempt'] > 1].sum()

    # Giờ nhân viên — số GIẢ LẬP (simulated).
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai

    tong = token + tool + xem_lai + lam_lai
    # Mẫu số: chỉ yêu cầu thực sự được giải quyết.
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())

    return dict(token=token, tool=tool, chay_lai=chay_lai,
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong,
                cps=tong / thanh_cong if thanh_cong else float('inf'),
                hoa_don_moi_yc=(token + tool) / len(reqs))


# ---------- Nhiệm vụ A3, A4 ----------
CHI_PHI_CO_DINH = 40_000_000   # đồng / tháng
YEU_CAU_THANG = 45_000         # yêu cầu hoàn phí / tháng ở quy mô đầy đủ
PHAM_VI = ['noi_dia', 'hang_nang']


def theo_loai(runs, reqs):
    """A3: chạy lại mo_hinh cho từng giá trị cột loai."""
    dong = []
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, r)
        so_lan_chay = runs['request_id'].isin(r['request_id']).sum()
        dong.append(dict(loai=loai, so_yc=len(r), ti_le_tc=kq['thanh_cong'] / len(r),
                         lan_chay_moi_yc=so_lan_chay / len(r), cps=kq['cps'],
                         so_voi_baseline=kq['cps'] / BASELINE))
    return pd.DataFrame(dong)


def chi_phi_co_dinh(runs, reqs, chi_phi_thang=CHI_PHI_CO_DINH, yc_thang=YEU_CAU_THANG):
    """A4: cộng chi phí cố định vào chi phí mỗi việc thành công trong phạm vi noi_dia + hang_nang."""
    pv = reqs[reqs['loai'].isin(PHAM_VI)]
    kq = mo_hinh(runs, pv)
    # Tỉ lệ việc thành công trong phạm vi trên TOÀN BỘ mẫu (45.000 là tổng mọi loại).
    ti_le = kq['thanh_cong'] / len(reqs)
    dong = []
    for ten, he_so in [('45.000 yêu cầu/tháng', 1.0), ('Một nửa khối lượng', 0.5)]:
        tc_thang = yc_thang * he_so * ti_le
        co_dinh = chi_phi_thang / tc_thang
        tong_moi_viec = kq['cps'] + co_dinh
        dong.append(dict(khoi_luong=ten, tc_thang=tc_thang, co_dinh_moi_viec=co_dinh,
                         cps_cong_co_dinh=tong_moi_viec, so_voi_baseline=tong_moi_viec / BASELINE))
    return kq, pd.DataFrame(dong)


# ---------- Nhiệm vụ B · Bảng độ nhạy ----------
KICH_BAN_B1 = {
    'Giá token gấp đôi':          dict(gia_vao=52, gia_ra=260),
    'Giá token giảm một nửa':     dict(gia_vao=13, gia_ra=65),
    'Tỉ lệ xem lại gấp đôi':      dict(he_so_xem_lai=2),
    'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
    'Số ca làm lại gấp đôi':      dict(he_so_lam_lai=2),
    'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
    'Lương nhân viên tăng 25%':   dict(luong_phut=2500),
    'Chỉ cho chạy tối đa 2 lần':  dict(max_lan_chay=2),
    'Chỉ cho chạy 1 lần':         dict(max_lan_chay=1),
}


def do_nhay(runs, reqs, kich_ban=KICH_BAN_B1):
    """B1/B2: mỗi kịch bản là một lần gọi mo_hinh với tham số đã đổi."""
    goc = mo_hinh(runs, reqs)['cps']
    dong = [dict(kich_ban='Gốc (A2)', cps=goc, thay_doi=0.0)]
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        dong.append(dict(kich_ban=ten, cps=cps, thay_doi=(cps / goc - 1) * 100))
    return pd.DataFrame(dong)


def gioi_han_chay(runs, reqs, cac_gioi_han=(1, 2, 3)):
    """B3: chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công
    (nhân viên phải làm thay)."""
    dong = []
    for k in cac_gioi_han:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - kq['thanh_cong']
        dong.append(dict(gioi_han=k, tong_tro_ly=kq['tong'], khong_tc=khong_tc,
                         ca_he_thong=kq['tong'] + khong_tc * BASELINE, cps=kq['cps']))
    return pd.DataFrame(dong)


def xem_lai_toan_bo(runs, reqs, phut_xem=5, phut_lam_lai=9, luong_phut=LUONG_PHUT):
    """B4: phạm vi noi_dia + hang_nang, mọi yêu cầu có ít nhất một lần chạy ok đều được xem lại."""
    pv = reqs[reqs['loai'].isin(PHAM_VI)]
    r = runs[runs['request_id'].isin(pv['request_id'])]
    token_tool = (r['tokens_in'] / 1000 * GIA_VAO + r['tokens_out'] / 1000 * GIA_RA
                  + r['tool_calls'] * GIA_TOOL).sum()
    so_xem = r.loc[r['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    thanh_cong = int((pv['ket_qua'] == 'thanh_cong').sum())
    tien_xem = so_xem * phut_xem * luong_phut
    tien_lam_lai = so_lam_lai * phut_lam_lai * luong_phut
    tong = token_tool + tien_xem + tien_lam_lai
    # Hoà vốn: số phút xem lại tối đa để chi phí mỗi việc thành công ≤ 12.000 đ.
    hoa_von = (BASELINE * thanh_cong - token_tool - tien_lam_lai) / (so_xem * luong_phut)
    return dict(so_yc=len(pv), so_xem=so_xem, tien_xem=tien_xem, so_lam_lai=so_lam_lai,
                tien_lam_lai=tien_lam_lai, token_tool=token_tool, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                so_voi_baseline=tong / thanh_cong / BASELINE, phut_xem_hoa_von=hoa_von)


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()

    # ----- A2 -----
    print('\n=== A2 · Mô hình chi phí từ trace (xem_lai, lam_lai, tong, cps: simulated) ===')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:15s} {gia_tri:>14,.1f}')
    tong = ket_qua['tong']
    print(f"cps / hoá đơn mỗi yêu cầu: {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f} lần")
    for k in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f'  tỉ trọng {k:8s} {ket_qua[k] / tong * 100:5.1f}%')
    print(f"  giờ nhân viên  {(ket_qua['xem_lai'] + ket_qua['lam_lai']) / tong * 100:5.1f}%")
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    he_thong = (tong + khong_tc * BASELINE) / len(reqs)
    print(f'Chi phí cả hệ thống / yêu cầu (cộng {khong_tc} ca nhân viên làm thay × 12.000): '
          f'{he_thong:,.0f} đ = {he_thong / BASELINE:.2f}× [simulated]')

    # ----- A3 -----
    print('\n=== A3 · Theo loại yêu cầu (cps: simulated) ===')
    a3 = theo_loai(runs, reqs)
    print(a3.to_string(index=False, formatters={
        'ti_le_tc': '{:.1%}'.format, 'lan_chay_moi_yc': '{:.2f}'.format,
        'cps': '{:,.0f}'.format, 'so_voi_baseline': '{:.2f}x'.format}))
    # Chạy lại có giúp không: tỉ lệ ok theo từng lần thử, theo loại.
    ok = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    ok['ok'] = (ok['status'] == 'ok').astype(float)
    print('\nTỉ lệ status = ok theo lần thử:')
    print(ok.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')
            .apply(lambda cot: cot.map('{:.1%}'.format)).to_string())

    # ----- A4 -----
    print('\n=== A4 · Chi phí cố định 40 triệu/tháng, phạm vi noi_dia + hang_nang (simulated) ===')
    kq_pv, a4 = chi_phi_co_dinh(runs, reqs)
    print(f"Trong phạm vi: tổng {kq_pv['tong']:,.0f} đ / {kq_pv['thanh_cong']} việc thành công "
          f"= {kq_pv['cps']:,.0f} đ")
    print(a4.to_string(index=False, formatters={
        'tc_thang': '{:,.0f}'.format, 'co_dinh_moi_viec': '{:,.0f}'.format,
        'cps_cong_co_dinh': '{:,.0f}'.format, 'so_voi_baseline': '{:.2f}x'.format}))

    # ----- B1 -----
    print('\n=== B1 · Đổi từng yếu tố (cps: simulated) ===')
    b1 = do_nhay(runs, reqs)
    print(b1.to_string(index=False, formatters={
        'cps': '{:,.0f}'.format, 'thay_doi': '{:+.1f}%'.format}))
    # Tự kiểm tra: mô hình tuyến tính → "giảm một nửa" = −½ mức tăng của "gấp đôi".
    tt = b1.set_index('kich_ban')['thay_doi']
    for gap_doi, giam_nua in [('Giá token gấp đôi', 'Giá token giảm một nửa'),
                              ('Tỉ lệ xem lại gấp đôi', 'Tỉ lệ xem lại giảm một nửa'),
                              ('Số ca làm lại gấp đôi', 'Số ca làm lại giảm một nửa')]:
        assert abs(tt[giam_nua] + tt[gap_doi] / 2) < 1e-9, f'{giam_nua} phải bằng −½ × {gap_doi}'
    print('Tự kiểm tra "giảm một nửa = −½ gấp đôi": ĐẠT')

    # ----- B2 -----
    print('\n=== B2 · Đổi một cặp: giá token gấp đôi + xem lại gấp đôi (simulated) ===')
    goc = ket_qua['cps']
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    tong_rieng = tt['Giá token gấp đôi'] + tt['Tỉ lệ xem lại gấp đôi']
    print(f'cps = {cap:,.0f} đ ({(cap / goc - 1) * 100:+.1f}%); '
          f'tổng hai tác động riêng = {tong_rieng:+.1f}%')
    # Xếp hạng theo độ lớn tác động khi yếu tố tăng (gấp đôi / +25%).
    tang = tt[['Giá token gấp đôi', 'Tỉ lệ xem lại gấp đôi', 'Số ca làm lại gấp đôi',
               'Lương nhân viên tăng 25%']].abs().sort_values(ascending=False)
    print('Xếp hạng:', ' · '.join(f'{i}. {ten} ({tt[ten]:+.1f}%)'
                                 for i, ten in enumerate(tang.index[:3], 1)))

    # ----- B3 -----
    print('\n=== B3 · Giới hạn số lần chạy và chi phí cả hệ thống (simulated) ===')
    b3 = gioi_han_chay(runs, reqs)
    print(b3.to_string(index=False, formatters={
        'tong_tro_ly': '{:,.0f}'.format, 'ca_he_thong': '{:,.0f}'.format,
        'cps': '{:,.0f}'.format}))
    re_nhat = b3.loc[b3['ca_he_thong'].idxmin()]
    cps_thap = b3.loc[b3['cps'].idxmin()]
    print(f"Rẻ nhất cho công ty: {re_nhat['gioi_han']:.0f} lần; "
          f"cps thấp nhất: {cps_thap['gioi_han']:.0f} lần "
          f"(đẩy thêm {cps_thap['khong_tc'] - re_nhat['khong_tc']:.0f} việc sang nhân viên)")

    # ----- B4 -----
    print('\n=== B4 · Xem lại 100% cho noi_dia + hang_nang (simulated) ===')
    lam_lai_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']
    print(f'Phút làm lại thực tế mỗi ca lam_lai: trung bình {lam_lai_tb.mean():.1f}, '
          f'trung vị {lam_lai_tb.median():.1f}')
    for phut in (9, round(lam_lai_tb.mean(), 1)):
        b4 = xem_lai_toan_bo(runs, reqs, phut_lam_lai=phut)
        print(f"Làm lại {phut} phút/ca: {b4['so_xem']} yc xem lại → {b4['tien_xem']:,.0f} đ; "
              f"{b4['so_lam_lai']} ca làm lại → {b4['tien_lam_lai']:,.0f} đ; "
              f"token+tool {b4['token_tool']:,.0f} đ; tổng {b4['tong']:,.0f} đ / "
              f"{b4['thanh_cong']} = {b4['cps']:,.0f} đ = {b4['so_voi_baseline']:.2f}×; "
              f"hoà vốn khi xem lại ≤ {b4['phut_xem_hoa_von']:.1f} phút")
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
