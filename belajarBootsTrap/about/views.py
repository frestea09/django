from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    context={
        'title':'About',
        'banner':'about/img/About.png',
        'content':"""
            

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vitae sodales est, faucibus semper neque. Nunc ut erat quis nisi eleifend scelerisque suscipit nec urna. Sed nec lectus tristique, vehicula turpis sed, dignissim augue. Etiam in accumsan odio, sed porttitor nulla. Ut arcu est, consectetur at ornare sit amet, cursus ac lorem. Suspendisse consequat ut lorem vel volutpat. Curabitur feugiat mauris turpis, eget blandit ipsum pulvinar sed. Phasellus consequat enim eget sagittis molestie. Mauris eget turpis iaculis libero mollis aliquet hendrerit vel massa. Curabitur ac placerat neque. Duis enim diam, cursus non ligula eget, eleifend auctor dolor.

Quisque auctor auctor purus vitae maximus. Nullam et sodales massa. Nullam finibus nulla et nibh pulvinar condimentum. Donec vel iaculis eros. Aenean molestie auctor nunc, id imperdiet nibh varius sit amet. Mauris a enim vitae urna iaculis hendrerit. Praesent aliquam velit pharetra, pulvinar leo in, consequat nisl. Donec auctor posuere tincidunt. Pellentesque sed ullamcorper orci. Vestibulum pharetra aliquam suscipit. Sed congue ex ligula, sed vulputate diam iaculis id. Curabitur ac sem porta, tristique quam quis, malesuada orci. Proin molestie eros dui, porttitor viverra diam fringilla non. Ut facilisis, sapien eu elementum elementum, augue lacus dictum quam, id malesuada urna felis sit amet metus. Nulla placerat lacinia justo, a luctus tellus porttitor vitae. Aliquam erat volutpat.

Vivamus est ipsum, molestie a facilisis eget, efficitur sagittis leo. Suspendisse ante nisi, lacinia porttitor cursus porttitor, tempus bibendum lectus. Pellentesque feugiat a velit nec hendrerit. Proin eget ipsum tellus. Donec eget finibus erat. Donec luctus mollis lorem et sodales. Integer ullamcorper purus eget odio iaculis eleifend. Fusce euismod sagittis porttitor. Aenean vel nunc eget nisi aliquam laoreet id sed urna. Phasellus non venenatis urna. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean consequat fermentum interdum. Pellentesque ac iaculis arcu. Nulla tempus nisl ut vulputate faucibus.

Mauris a justo magna. Ut dapibus bibendum odio ac accumsan. Etiam condimentum ante a consectetur vestibulum. Aliquam blandit felis nec odio faucibus, viverra vehicula arcu viverra. Etiam felis felis, porta non viverra eget, fermentum vitae nunc. Aenean vehicula faucibus pharetra. Nulla sed vehicula lorem.

Morbi rhoncus sit amet ante eu tincidunt. Suspendisse velit nulla, ullamcorper ut elementum at, tristique a risus. Aliquam sodales blandit erat ac eleifend. Quisque egestas ligula neque, vel sodales tellus ullamcorper eu. Aliquam scelerisque ut arcu quis mollis. Etiam tempus, mauris a molestie interdum, dui libero accumsan diam, semper ultrices massa neque non metus. Donec tempus elit sit amet tellus blandit condimentum. Etiam blandit metus sagittis justo eleifend, a lobortis mauris suscipit. Pellentesque nec nulla lobortis, fermentum enim eu, blandit mauris. Cras lorem tellus, vestibulum vitae malesuada eget, dignissim nec lectus. Nullam eget est eu mauris accumsan cursus at ac nulla. Fusce accumsan fermentum enim mattis ullamcorper. Nulla facilisis sem vel consectetur scelerisque. Aliquam viverra, metus nec convallis tempor, mauris diam tempus mi, ac tempus est dui vitae justo. Proin ut ex ac orci bibendum faucibus sed quis lacus. Duis fringilla tempus rutrum. 
        """,
        'nav':[
            ['/home','Home'],
            ['/about','About'],
            ['/blog','Blog'],
            ['/music','Music'],
        ],
        'about_style':'about/css/styles.css',
        'style': 'css/styles.css',
        'author':'ilman teguh prasetya',
        'date':datetime.datetime.now(),
    }
    return render(request,'about/index.html',context)