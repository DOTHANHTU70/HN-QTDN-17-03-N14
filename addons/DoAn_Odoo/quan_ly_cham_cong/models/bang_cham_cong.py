from odoo import models, fields, api


class BangChamCong(models.Model):
    _name = 'bang_cham_cong'
    _description = 'Bảng chấm công tháng'
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
        compute='_compute_tong_hop',
        store=True
    )

    so_ngay_vang = fields.Integer(
        string='Số ngày vắng',
        compute='_compute_tong_hop',
        store=True
    )

    so_ngay_nghi_phep = fields.Integer(
        string='Số ngày nghỉ phép',
        compute='_compute_tong_hop',
        store=True
    )
    trang_thai = fields.Selection(
    [
        ('nhap', 'Nháp'),
        ('da_chot', 'Đã chốt')
    ],
    string='Trạng thái',
    default='nhap'
)

    @api.depends('nhan_vien_id', 'thang', 'nam')
    def _compute_tong_hop(self):
        for rec in self:
            rec.so_cong = 0
            rec.so_ngay_vang = 0
            rec.so_ngay_nghi_phep = 0

            if not rec.nhan_vien_id:
                continue

            ngay_bat_dau = f"{rec.nam}-{rec.thang:02d}-01"

            if rec.thang == 12:
                ngay_ket_thuc = f"{rec.nam + 1}-01-01"
            else:
                ngay_ket_thuc = f"{rec.nam}-{rec.thang + 1:02d}-01"

            ds_cham_cong = self.env['hr_cham_cong'].search([
                ('nhan_vien_id', '=', rec.nhan_vien_id.id),
                ('ngay_cham_cong', '>=', ngay_bat_dau),
                ('ngay_cham_cong', '<', ngay_ket_thuc),
            ])

            for cc in ds_cham_cong:
                if cc.trang_thai == 'co_mat':
                    rec.so_cong += 1
                elif cc.trang_thai == 'vang':
                    rec.so_ngay_vang += 1
                elif cc.trang_thai == 'nghi_phep':
                    rec.so_ngay_nghi_phep += 1

    def action_chot_cong(self):
        for rec in self:
            if rec.trang_thai == 'da_chot':
                continue

            rec.trang_thai = 'da_chot'
           

        
    _sql_constraints = [
        (
            'unique_bang_cham_cong',
            'unique(nhan_vien_id, thang, nam)',
            'Bảng chấm công tháng này đã tồn tại!'
        )
    ]