from odoo import models, fields


class HRDangKyCa(models.Model):
    _name = 'hr_dang_ky_ca'
    _description = 'Đăng ký ca'
    _rec_name = 'nhan_vien_id'

    nhan_vien_id = fields.Many2one(
        'nhan_vien',
        string='Nhân viên',
        required=True
    )

    dot_dang_ky_id = fields.Many2one(
        'hr_dot_dang_ky',
        string='Đợt đăng ký',
        required=True
    )

    ngay_lam = fields.Date(
        string='Ngày làm',
        required=True,
        default=fields.Date.today
    )

    ca_lam = fields.Selection([
        ('sang', 'Ca sáng'),
        ('chieu', 'Ca chiều'),
        ('toi', 'Ca tối')
    ],
    string='Ca làm',
    required=True)

    trang_thai = fields.Selection([
        ('cho_duyet', 'Chờ duyệt'),
        ('da_duyet', 'Đã duyệt'),
        ('tu_choi', 'Từ chối')
    ],
    string='Trạng thái',
    default='cho_duyet')