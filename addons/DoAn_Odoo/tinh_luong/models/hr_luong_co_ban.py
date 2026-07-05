from odoo import models, fields


class HRLuongCoBan(models.Model):
    _name = 'hr_luong_co_ban'
    _description = 'Lương cơ bản'
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

    luong_co_ban = fields.Float(
        string='Lương cơ bản',
        required=True
    )

    phu_cap_an_trua = fields.Float(
        string='Phụ cấp ăn trưa',
        default=0
    )

    phu_cap_trach_nhiem = fields.Float(
        string='Phụ cấp trách nhiệm',
        default=0
    )