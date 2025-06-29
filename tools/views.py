from django.shortcuts import render, get_object_or_404
from .models import Tool
from django.db.models import Q 
from .models import Tutorial
from django.utils.text import slugify





def tool_list(request):
    query = request.GET.get('q')
    selected_category = request.GET.get('category')
    tools = Tool.objects.all()

    if query:
        tools = tools.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query) |
            Q(tags__icontains=query)
        ).distinct()

    if selected_category and selected_category != 'All':
        tools = tools.filter(category__iexact=selected_category)

    categories = Tool.objects.values_list('category', flat=True).distinct()

    return render(request, 'tools/tool_list.html', {
        'tools': tools,
        'query': query,
        'categories': categories,
        'selected_category': selected_category,
    })


# def categories_page(request):
#     categories = Tool.objects.values_list('category', flat=True).distinct().exclude(category__exact='').order_by('category')
#     return render(request, 'tools/categories.html', {'categories': categories})

def tools_by_category(request, slug):
    from .models import Tool
    all_categories = Tool.objects.values_list('category', flat=True).distinct()
    
    matching_category = None
    for cat in all_categories:
        if slugify(cat) == slug:
            matching_category = cat
            break

    if not matching_category:
        return render(request, 'tools/category_tools.html', {
            'tools': [],
            'category_name': "Not Found"
        })

    tools = Tool.objects.filter(category__iexact=matching_category)

    return render(request, 'tools/category_tools.html', {
        'tools': tools,
        'category_name': matching_category
    })


CATEGORY_IMAGES = {
    "AI Writing": "https://images.unsplash.com/photo-1581090700227-1e8a5f07c9b9?auto=format&fit=crop&w=800&q=80",
    "Text-to-Speech": "https://images.unsplash.com/photo-1581093588401-058c7a8d17b2?auto=format&fit=crop&w=800&q=80",
    "Text-to-Image": "https://images.unsplash.com/photo-1627745814073-7e8a750caf5e?auto=format&fit=crop&w=800&q=80",
    "AI Chatbots": "https://images.unsplash.com/photo-1559138801-bf9557b2f321?auto=format&fit=crop&w=800&q=80",
    "Video Generation": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80",
    "Image Editing": "https://images.unsplash.com/photo-1497493292307-31c376b6e479?auto=format&fit=crop&w=800&q=80",
    "Code Generation": "https://images.unsplash.com/photo-1581090700187-e1cc7c1872b2?auto=format&fit=crop&w=800&q=80",
    "Content Creation": "https://images.unsplash.com/photo-1616587897288-3c353d76a77d?auto=format&fit=crop&w=800&q=80",
    "AI Productivity": "https://images.unsplash.com/photo-1531497865144-0464ef8fb9c9?auto=format&fit=crop&w=800&q=80",
    "AI Art": "https://images.unsplash.com/photo-1615394953594-f8e8f1d1f63b?auto=format&fit=crop&w=800&q=80",
}

def categories_page(request):
    from .models import Tool
    categories = Tool.objects.values_list('category', flat=True).distinct().exclude(category__exact='').order_by('category')
    
    category_data = []
    for cat in categories:
        category_data.append({
            'name': cat,
            'slug': slugify(cat),
            'image': CATEGORY_IMAGES.get(cat, "https://via.placeholder.com/300x200?text=AI+Category")
        })

    return render(request, 'tools/categories.html', {
        'categories': category_data
    })






def tutorials_page(request):
    return render(request, 'tools/tutorials.html')

def about_page(request):
    return render(request, 'tools/about.html')



def tool_detail(request, tool_id):
    tool = get_object_or_404(Tool, id=tool_id)
    return render(request, 'tools/tool_detail.html', {'tool': tool})





# Create your views here.


def tutorials_page(request):
    tutorials = Tutorial.objects.select_related('tool').order_by('-published_at')
    return render(request, 'tools/tutorials.html', {'tutorials': tutorials})


def tutorial_detail(request, pk):
    tutorial = Tutorial.objects.select_related('tool').get(pk=pk)
    return render(request, 'tools/tutorial_detail.html', {'tutorial': tutorial})



