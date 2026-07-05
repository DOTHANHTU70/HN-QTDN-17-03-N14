from odoo import models, fields


class HRThamSoLuong(models.Model):
    _name = 'hr_tham_so_luong'
    _description = 'Tham số lương'
    _rec_name = 'ten'

    ten = fields.Char(
        string='Tên cấu hình',
        required=True,
        default='Cấu hình mặc định'
    )

    cong_chuan = fields.Integer(
        string='Công chuẩn',
        default=26,
        required=True
    )

    bhxh = fields.Float(
        string='BHXH (%)',
        default=8.0
    )

    bhyt = fields.Float(
        string='BHYT (%)',
        default=1.5
    )

    bhtn = fields.Float(
        string='BHTN (%)',
        default=1.0
    )

    ot_ngay_thuong = fields.Float(
        string='OT ngày thường (%)',
        default=150.0
    )

    ot_cuoi_tuan = fields.Float(
        string='OT cuối tuần (%)',
        default=200.0
    )

    ot_ngay_le = fields.Float(
        string='OT ngày lễ (%)',
        default=300.0
    )