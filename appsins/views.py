from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    #print (request.POST.get('item_text', ''))
    lista = []
    if not request.POST.get('item_text') == 'B00000000':
        if request.POST.get('item_text'):
            target = open('/Users/jerbiguy/Perl/Amazon/Squating/Scripts_For_Site/asins.cfg', 'w')
            target.truncate()
            target.write(request.POST.get('item_text'))
            target.close()
            import subprocess
            var = "/Users/jerbiguy/Perl/Amazon/Squating/Scripts_For_Site/"
            #pipe = subprocess.Popen(["perl", "get_data_per_asin.pl", var]).communicate()[0]
            pipe = subprocess.Popen(["perl", "/Users/jerbiguy/Perl/Amazon/Squating/Scripts_For_Site/get_data_per_asin.pl"]).communicate()[0]
            with open('/Users/jerbiguy/Perl/Amazon/Squating/Scripts_For_Site/load_db_with.txt','r') as f:
                lines = (line.strip() for line in f)
                for line in lines:
                    lista=line.split(',')
#with open('./load_db_with.txt','r') as f:
#    lines = (line.strip() for line in f)
#    for line in lines:
#        print(line)
    if len(lista) == 0:
        return render(request, 'base.html', {
        'new_item_text': request.POST.get('item_text', ''), ### catching the post from the request by it's input name="item_text" - not value !!!! 
        })
    else:
        return render(request, 'response.html', {
        #'new_item_text': request.POST.get('item_text', ''), ### catching the post from the request by it's input name="item_text" - not value !!!!·
            'new_item_text': lista, ### catching the post from the request by it's input name="item_text" - not value !!!!·
        })
