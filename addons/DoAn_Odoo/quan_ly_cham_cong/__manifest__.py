{
    'name': 'Quản lý Chấm công',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Quản lý chấm công nhân viên',
    'depends': [
        'base',
        'nhan_su',
        
    ],
        'data': [
        'security/ir.model.access.csv',
        'views/hr_cham_cong_views.xml',
        'views/bang_cham_cong_views.xml',
        'views/hr_don_tu_views.xml',
        'views/hr_dot_dang_ky_views.xml',
        'views/hr_dang_ky_ca_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
