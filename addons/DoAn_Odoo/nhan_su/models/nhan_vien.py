from odoo import models, fields

class NhanVien(models.Model):
    _name = 'nhan_vien'
    _description = 'Nhân viên'
    _rec_name = 'ho_ten'

    ma_dinh_danh = fields.Char(string='Mã định danh', required=True)
    ho_ten = fields.Char(string='Họ tên')
    ngay_sinh = fields.Date(string='Ngày sinh')
    que_quan = fields.Char(string='Quê quán')
    email = fields.Char(string='Email')
    _sql_constraints = [
    (
        'unique_ma_dinh_danh',
        'unique(ma_dinh_danh)',
        'Mã định danh đã tồn tại!'
    ),
]