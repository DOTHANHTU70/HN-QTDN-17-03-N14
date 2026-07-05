from odoo import models, fields


class HRDotDangKy(models.Model):
    _name = 'hr_dot_dang_ky'
    _description = 'Đợt đăng ký ca'
    _rec_name = 'ten_dot'

    ten_dot = fields.Char(
        string='Tên đợt',
        required=True
    )

    ngay_bat_dau = fields.Date(
        string='Ngày bắt đầu',
        required=True
    )

    ngay_ket_thuc = fields.Date(
        string='Ngày kết thúc',
        required=True
    )

    trang_thai = fields.Selection([
        ('mo', 'Mở'),
        ('dong', 'Đóng')
    ],
    string='Trạng thái',
    default='mo')