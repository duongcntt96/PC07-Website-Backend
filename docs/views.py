from django.shortcuts import render
from django.http import HttpResponse

from .models import Doc


# def doc(request, id):
#     # Lấy danh sách nhập kho
#     from qlpt.models import Phieu_nhap
#     phieu_nhap = Phieu_nhap.objects.filter(success=True)

#     # Lấy danh sách phương tiện đã nhập
#     from qlpt.models import Chi_tiet_phieu_nhap, Danh_muc_phuong_tien
#     from django.db.models import Sum
#     phuong_tien_nhap = Chi_tiet_phieu_nhap.objects.values('phuong_tien').annotate(
#         totals=Sum('so_luong'))
#     phuong_tien_xuat = Chi_tiet_phieu_xuat.objects.values('phuong_tien', 'phuong_tien__chung_loai', 'phuong_tien__ten').annotate(
#         totals=Sum('so_luong'))

#     for pt in phuong_tien_nhap:
#         print('phuong tien: ' + str(pt['totals']))
#         _xuat = phuong_tien_xuat.filter(phuong_tien=pt['phuong_tien'])
#         if _xuat:
#             print(_xuat[0]['totals'])
#             pt['totals'] = pt['totals']-_xuat[0]['totals']

#     data = {
#         "phieu_nhap": phieu_nhap,
#         "phuong_tien_nhap": phuong_tien_nhap,
#         "phuong_tien_xuat": phuong_tien_xuat,
#     }

#     return render(request, 'docs/doc.html', data)


def docx_viewer(request, id):
    import mammoth
    doc = Doc.objects.get(id=id)
    html = docx2html(doc.file)
    return HttpResponse("<div style='width: 800px'>" + html + "</div>")


def docx2html(input_filename):
    import mammoth
    # input_filename = "a.docx"
    custom_styles = """ b => b.mark
	                    u => u.initialism
	                    p[style-name='Heading 1'] => h1.card
	                    table => table.table.table-hover
	                    """
    # bootstrap_css = '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">'
    # bootstrap_js = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>'

    with input_filename.open(mode='rb') as docx_file:
        result = mammoth.convert_to_html(docx_file, style_map=custom_styles)
        html = result.value

    edited_html = html  # bootstrap_css + html + bootstrap_js
    # print(edited_html)

    output_filename = "output.html"
    with open(output_filename, mode="w", encoding="utf-8") as f:
        f.writelines(edited_html)
    return edited_html
