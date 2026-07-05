from odoo import models, fields


class HRDonTu(models.Model):
    _name = 'hr_don_tu'
    _description = 'Đơn từ nhân viên'
    _rec_name = 'nhan_vien_id'

    nhan_vien_id = fields.Many2one(
        'nhan_vien',
        string='Nhân viên',
        required=True
    )

    loai_don = fields.Selection([
        ('nghi_phep', 'Nghỉ phép'),
        ('di_muon', 'Đi muộn'),
        ('ve_som', 'Về sớm'),
        ('tang_ca', 'Tăng ca'),
    ],
    string='Loại đơn',
    required=True)

    ngay = fields.Date(
        string='Ngày',
        required=True,
        default=fields.Date.today
    )

    ly_do = fields.Text(
        string='Lý do'
    )

    trang_thai = fields.Selection([
        ('cho_duyet', 'Chờ duyệt'),
        ('da_duyet', 'Đã duyệt'),
        ('tu_choi', 'Từ chối'),
    ],
    string='Trạng thái',
    default='cho_duyet'
    )

    nguoi_duyet = fields.Char(
        string='Người duyệt',
        readonly=True
    )

    ngay_duyet = fields.Date(
        string='Ngày duyệt',
        readonly=True
    )

    def action_duyet(self):
        for rec in self:
            rec.write({
                'trang_thai': 'da_duyet',
                'nguoi_duyet': self.env.user.name,
                'ngay_duyet': fields.Date.today(),
            })

    def action_tu_choi(self):
        for rec in self:
            rec.write({
                'trang_thai': 'tu_choi',
                'nguoi_duyet': self.env.user.name,
                'ngay_duyet': fields.Date.today(),
            })