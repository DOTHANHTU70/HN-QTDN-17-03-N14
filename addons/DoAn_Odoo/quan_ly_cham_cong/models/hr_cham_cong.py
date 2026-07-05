from odoo import models, fields


class HRChamCong(models.Model):
    _name = 'hr_cham_cong'
    _description = 'Chấm công nhân viên'
    _rec_name = 'nhan_vien_id'

    nhan_vien_id = fields.Many2one(
        'nhan_vien',
        string='Nhân viên',
        required=True
    )

    ngay_cham_cong = fields.Date(
        string='Ngày chấm công',
        required=True,
        default=fields.Date.today
    )

    trang_thai = fields.Selection(
        [
            ('co_mat', 'Có mặt'),
            ('vang', 'Vắng'),
            ('nghi_phep', 'Nghỉ phép')
        ],
        string='Trạng thái',
        default='co_mat',
        required=True
    )

    ghi_chu = fields.Text(
        string='Ghi chú'
    )
