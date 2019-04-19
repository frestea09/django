from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    context={
        'title':'Blog',
        'header':'Blog',
        'date': datetime.datetime.now(),
        'author':'ilman teguh prasetya',
        'banner':'img/Blog.png',
        'style_blog':'css/styles.css',
        'nav':[
          ['/home','Home'],
            ['/about','About'],
            ['/blog','Blog'],
            ['/introduction','Introduction'],
            ['/music','Music'],
        ],
        'article':'''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut dictum congue neque, tincidunt blandit mauris bibendum ut. Fusce hendrerit, tellus et tincidunt posuere, ligula justo aliquet mi, et viverra metus eros mollis libero. Sed tempus faucibus condimentum. Etiam varius fringilla justo, vel efficitur ligula tempus a. Aenean efficitur lectus ac lectus viverra, sed tristique leo viverra. In hac habitasse platea dictumst. Pellentesque ac neque nisl. Pellentesque convallis sem non velit varius faucibus. Vivamus lacus ex, semper in maximus sit amet, pulvinar vitae lacus. Suspendisse eu blandit mauris. Praesent pretium purus eu vehicula molestie. Morbi fermentum, neque vel bibendum viverra, enim tortor ornare arcu, ut gravida nibh odio et ante. Phasellus quis leo ex. In pharetra nisi in tortor convallis egestas. Morbi et tortor ipsum. Nunc euismod diam diam, sit amet auctor nulla semper et.

Phasellus congue ante sem, consequat ullamcorper sem blandit nec. Ut dui lectus, interdum sit amet commodo at, vulputate ut orci. Aenean metus lorem, congue ac ligula ac, rutrum sodales justo. Donec et nulla a ex viverra tristique. Phasellus eu sem nisl. Praesent porttitor nulla elit, a blandit est euismod porta. Integer vulputate fringilla quam, at ultricies purus lobortis vitae. Ut accumsan id dolor quis suscipit. Quisque non sapien congue, faucibus velit nec, tempus sapien. Sed tortor nunc, luctus vel nibh quis, gravida dignissim sem. Sed maximus sed velit et maximus. Vestibulum venenatis condimentum ultrices. Maecenas porttitor nulla nibh, et gravida lectus feugiat sit amet.

Nullam ac ultrices odio, eget vestibulum velit. Ut eget purus sed elit finibus commodo id in dui. Aenean sollicitudin felis eget finibus sodales. Cras sed ante lacinia est sodales accumsan. Nunc dapibus arcu sit amet justo luctus pulvinar. Mauris suscipit vitae tortor ut mattis. Cras tincidunt vestibulum nibh eget sollicitudin. Nulla in sem elementum, congue nibh nec, elementum augue. Suspendisse lobortis luctus massa sed convallis. Donec sit amet quam pharetra tellus blandit posuere. Nulla facilisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc molestie auctor urna, sed vulputate neque maximus ut. Sed fringilla, leo ac maximus gravida, ligula turpis fringilla risus, commodo hendrerit metus mauris eget massa. Quisque pulvinar neque tincidunt, scelerisque leo at, dignissim nibh.

Quisque pharetra maximus ex a bibendum. Aliquam erat volutpat. Etiam mollis viverra faucibus. Sed facilisis lorem at egestas vulputate. Suspendisse ut felis sit amet diam pretium venenatis vel at ligula. Praesent consectetur non ipsum vitae mattis. Mauris semper fermentum pulvinar. Nam libero nulla, commodo sed risus ut, lacinia malesuada odio. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam commodo, enim at varius facilisis, mi nisi aliquam leo, id semper ante mauris nec lectus.

Aenean posuere varius eros ac rhoncus. Praesent vestibulum condimentum tortor ac dignissim. Nullam a ultrices ex. Nulla porttitor rutrum rhoncus. Sed fermentum, lectus vulputate sagittis varius, sapien eros scelerisque eros, eget varius elit libero at magna. Aenean egestas, erat eu dignissim pretium, velit odio egestas tellus, ac laoreet velit dui ac nisi. Duis pellentesque nisl nisl, non dictum est ornare sed. Donec blandit lacus nec lectus viverra, non aliquam nisi malesuada. Nunc feugiat id nunc eget feugiat. 
        ''',
    }
    return render(request,'blog/index.html',context)