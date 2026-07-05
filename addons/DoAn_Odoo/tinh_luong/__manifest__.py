{
    'name': 'Tính lương',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Quản lý lương nhân viên',

    'depends': [
        'base',
        'nhan_su',
        'quan_ly_cham_cong',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/hr_luong_co_ban_views.xml',
        'views/hr_bang_luong_views.xml',
        'views/hr_hop_dong_views.xml',
        'views/hr_tham_so_luong_views.xml',
        'views/hr_phieu_luong_views.xml',
        'views/menu.xml',
    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}