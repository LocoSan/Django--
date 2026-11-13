from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .forms import PreferencesForm, SIZES, STYLES

PRODUCTS = [
    {"name": "Льняная рубашка", "style": "classic", "sizes": ["S", "M", "L"],
     "price": 2490, "image": "catalog/shirt.svg", "description": "Светлая рубашка на каждый день."},
    {"name": "Спортивная футболка", "style": "sport", "sizes": ["M", "L", "XL"],
     "price": 1290, "image": "catalog/tshirt.svg", "description": "Лёгкая футболка для тренировок."},
    {"name": "Худи с капюшоном", "style": "casual", "sizes": ["S", "M", "XL"],
     "price": 2990, "image": "catalog/hoodie.svg", "description": "Мягкое худи свободного кроя."},
]


def catalog(request):
    style = request.COOKIES.get("style", "")
    size = request.COOKIES.get("size", "")
    if style not in dict(STYLES):
        style = ""
    if size not in dict(SIZES):
        size = ""

    if request.method == "POST":
        form = PreferencesForm(request.POST)
        if form.is_valid():
            response = redirect("catalog")
            for name in ("style", "size"):
                response.set_cookie(name, form.cleaned_data[name], max_age=30 * 86400,
                                    httponly=True, samesite="Lax")
            return response
    else:
        form = PreferencesForm(initial={"style": style, "size": size})

    products = [
        {**product, "style_label": dict(STYLES)[product["style"]]}
        for product in PRODUCTS
        if (not style or style == product["style"]) and (not size or size in product["sizes"])
    ]
    return render(request, "catalog/index.html", {"form": form, "products": products})


@require_POST
def reset(request):
    response = redirect("catalog")
    response.delete_cookie("style", samesite="Lax")
    response.delete_cookie("size", samesite="Lax")
    return response
