from odoo import models, fields


class HRPhieuLuong(models.Model):
    _name = 'hr_phieu_luong'
    _description = 'Phiếu lương'
    _rec_name = 'nhan_vien_id'

    bang_luong_id = fields.Many2one(
        'hr_bang_luong',
        string='Bảng lương',
        required=True
    )

    nhan_vien_id = fields.Many2one(
        'nhan_vien',
        string='Nhân viên',
        related='bang_luong_id.nhan_vien_id',
        store=True
    )

    thang = fields.Integer(
        string='Tháng',
        related='bang_luong_id.thang',
        store=True
    )

    nam = fields.Integer(
        string='Năm',
        related='bang_luong_id.nam',
        store=True
    )

    so_cong = fields.Integer(
        string='Số công',
        related='bang_luong_id.so_cong',
        store=True
    )

    tong_phu_cap = fields.Float(
        string='Tổng phụ cấp',
        related='bang_luong_id.tong_phu_cap',
        store=True
    )

    thuong = fields.Float(
        string='Thưởng',
        related='bang_luong_id.thuong',
        store=True
    )

    khau_tru = fields.Float(
        string='Khấu trừ',
        related='bang_luong_id.khau_tru',
        store=True
    )

    tien_bhxh = fields.Float(
        string='BHXH',
        related='bang_luong_id.tien_bhxh',
        store=True
    )

    tien_bhyt = fields.Float(
        string='BHYT',
        related='bang_luong_id.tien_bhyt',
        store=True
    )

    tien_bhtn = fields.Float(
        string='BHTN',
        related='bang_luong_id.tien_bhtn',
        store=True
    )

    luong_thuc_nhan = fields.Float(
        string='Lương thực nhận',
        related='bang_luong_id.luong_thuc_nhan',
        store=True
    )