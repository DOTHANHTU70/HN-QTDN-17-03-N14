from odoo import models, fields, api


class HRBangLuong(models.Model):
    _name = 'hr_bang_luong'
    _description = 'Bảng lương'
    _rec_name = 'nhan_vien_id'

    nhan_vien_id = fields.Many2one(
        'nhan_vien',
        string='Nhân viên',
        required=True
    )

    ma_dinh_danh = fields.Char(
        string='Mã định danh',
        related='nhan_vien_id.ma_dinh_danh',
        store=True
    )

    thang = fields.Integer(
        string='Tháng',
        required=True,
        default=lambda self: fields.Date.today().month
    )

    nam = fields.Integer(
        string='Năm',
        required=True,
        default=lambda self: fields.Date.today().year
    )

    so_cong = fields.Integer(
        string='Số công',
        compute='_compute_luong',
        store=True
    )

    tong_phu_cap = fields.Float(
        string='Tổng phụ cấp',
        compute='_compute_luong',
        store=True
    )

    luong_theo_cong = fields.Float(
        string='Lương theo công',
        compute='_compute_luong',
        store=True
    )

    thuong = fields.Float(
        string='Thưởng',
        default=0.0
    )

    khau_tru = fields.Float(
        string='Khấu trừ',
        default=0.0
    )

    tien_bhxh = fields.Float(
        string='BHXH',
        compute='_compute_luong',
        store=True
    )

    tien_bhyt = fields.Float(
        string='BHYT',
        compute='_compute_luong',
        store=True
    )

    tien_bhtn = fields.Float(
        string='BHTN',
        compute='_compute_luong',
        store=True
    )

    tong_bao_hiem = fields.Float(
        string='Tổng bảo hiểm',
        compute='_compute_luong',
        store=True
    )

    luong_thuc_nhan = fields.Float(
        string='Lương thực nhận',
        compute='_compute_luong',
        store=True
    )

    @api.depends(
        'nhan_vien_id',
        'thang',
        'nam',
        'thuong',
        'khau_tru'
    )
    def _compute_luong(self):
        for rec in self:
            rec.so_cong = 0
            rec.tong_phu_cap = 0
            rec.luong_theo_cong = 0

            rec.tien_bhxh = 0
            rec.tien_bhyt = 0
            rec.tien_bhtn = 0
            rec.tong_bao_hiem = 0

            rec.luong_thuc_nhan = 0

            if not rec.nhan_vien_id:
                continue

            # Xác định khoảng thời gian của tháng
            ngay_bat_dau = f"{rec.nam}-{rec.thang:02d}-01"

            if rec.thang == 12:
                ngay_ket_thuc = f"{rec.nam + 1}-01-01"
            else:
                ngay_ket_thuc = f"{rec.nam}-{rec.thang + 1:02d}-01"

            # Đếm số ngày có mặt
            cham_cong = self.env['hr_cham_cong'].search([
                ('nhan_vien_id', '=', rec.nhan_vien_id.id),
                ('trang_thai', '=', 'co_mat'),
                ('ngay_cham_cong', '>=', ngay_bat_dau),
                ('ngay_cham_cong', '<', ngay_ket_thuc),
            ])

            rec.so_cong = len(cham_cong)

            # Lấy cấu hình lương
            luong = self.env['hr_luong_co_ban'].search([
                ('nhan_vien_id', '=', rec.nhan_vien_id.id)
            ], limit=1)

            # Lấy tham số lương
            tham_so = self.env['hr_tham_so_luong'].search([], limit=1)

            if luong:
                rec.tong_phu_cap = (
                    luong.phu_cap_an_trua
                    + luong.phu_cap_trach_nhiem
                )

                tong_luong = (
                    luong.luong_co_ban
                    + rec.tong_phu_cap
                )

                cong_chuan = tham_so.cong_chuan if tham_so else 26

                rec.luong_theo_cong = (
                    tong_luong * rec.so_cong / cong_chuan
                    )

                # Tính bảo hiểm
                if tham_so:
                    rec.tien_bhxh = (
                        luong.luong_co_ban
                        * tham_so.bhxh / 100
                    )

                    rec.tien_bhyt = (
                        luong.luong_co_ban
                        * tham_so.bhyt / 100
                    )

                    rec.tien_bhtn = (
                        luong.luong_co_ban
                        * tham_so.bhtn / 100
                    )

                    rec.tong_bao_hiem = (
                        rec.tien_bhxh
                        + rec.tien_bhyt
                        + rec.tien_bhtn
                    )

                rec.luong_thuc_nhan = (
                    rec.luong_theo_cong
                    + rec.thuong
                    - rec.khau_tru
                    - rec.tong_bao_hiem
                )
                
    def action_tao_phieu_luong(self):
        for rec in self:
            phieu = self.env['hr_phieu_luong'].search([
                ('bang_luong_id', '=', rec.id)
            ], limit=1)

            if phieu:
                continue

            self.env['hr_phieu_luong'].create({
                'bang_luong_id': rec.id,
            })