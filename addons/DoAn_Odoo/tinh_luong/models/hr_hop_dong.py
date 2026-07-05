from odoo import models, fields


class HRHopDong(models.Model):
    _name = 'hr_hop_dong'
    _description = 'Hợp đồng lao động'
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

    loai_hop_dong = fields.Selection([
        ('thu_viec', 'Thử việc'),
        ('xac_dinh_thoi_han', 'Xác định thời hạn'),
        ('khong_xac_dinh', 'Không xác định thời hạn'),
    ],
    string='Loại hợp đồng',
    required=True)

    ngay_bat_dau = fields.Date(
        string='Ngày bắt đầu',
        required=True
    )

    ngay_ket_thuc = fields.Date(
        string='Ngày kết thúc'
    )

    luong_thoa_thuan = fields.Float(
        string='Lương thỏa thuận',
        required=True
    )

    trang_thai = fields.Selection([
        ('hieu_luc', 'Hiệu lực'),
        ('het_han', 'Hết hạn'),
        ('tam_dung', 'Tạm dừng'),
    ],
    string='Trạng thái',
    default='hieu_luc'
    )

    ghi_chu = fields.Text(
        string='Ghi chú'
    )