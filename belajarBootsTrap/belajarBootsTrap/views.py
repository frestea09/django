from django.shortcuts import render
import datetime
def index(request):
    context={
        'title':'Home',
        'content':'''
        
Lorem ipsum dolor sit amet, consWectetur adipiscing elit. Aliquam aliquet ac lectus nec faucibus. Etiam semper lorem vitae porta mattis. Donec accumsan vehicula ultrices. Nulla efficitur sodales dolor placerat pretium. Praesent nec turpis sagittis augue imperdiet ornare. Morbi sed felis et augue vulputate porta. Nulla finibus tellus et nunc tincidunt tempus. Pellentesque eleifend mauris maximus aliquam placerat. Proin sodales consequat ex, sed rhoncus lorem molestie eget. Vivamus ultrices justo et lacus hendrerit, at congue justo suscipit. Suspendisse lacinia, augue eget imperdiet mattis, sem neque sagittis mi, sodales dignissim ante mauris sed magna. Suspendisse potenti. Ut quis tincidunt nisl, at porttitor nisi. Maecenas ut enim vehicula, accumsan justo et, luctus dui. Praesent egestas convallis luctus. Integer aliquam pulvinar lectus, sit amet volutpat nibh rhoncus vitae.

In consectetur ante iaculis, consectetur quam et, rhoncus dui. Phasellus volutpat vel ante at sagittis. Nullam ac erat eget dui malesuada fermentum. Ut posuere pretium turpis, at sollicitudin lectus molestie sed. In nisl dui, consectetur ut scelerisque posuere, laoreet at diam. Ut ipsum mauris, tincidunt mollis ante eget, luctus placerat augue. Curabitur id enim a ligula cursus ultrices. Mauris eget quam id diam ultrices tincidunt eu quis ipsum. Pellentesque massa leo, commodo vel neque vel, sodales fermentum erat. Ut ac orci imperdiet, ultrices justo at, faucibus sapien. Etiam malesuada, mi eu fermentum cursus, metus ante eleifend quam, id facilisis eros quam at nulla.

Praesent vel lacus pulvinar nulla consectetur accumsan. Integer mauris felis, auctor et nibh et, euismod rhoncus arcu. Pellentesque nisi libero, maximus vitae molestie nec, fringilla eu nulla. Nunc a risus sed enim ultrices tincidunt nec quis lorem. Etiam et ornare diam. Duis augue eros, efficitur eu dui ut, porta aliquet tortor. Suspendisse quis odio egestas, lobortis nisl nec, tempor quam. Maecenas diam urna, pellentesque in nunc quis, laoreet semper ex. Sed viverra ut erat in fringilla. Integer mattis, dolor et pretium euismod, purus justo sodales nulla, eu consequat dui lacus id nisl. Curabitur sed ante at metus facilisis egestas vitae quis augue.

Vivamus imperdiet at est sit amet porta. Fusce sapien massa, tempus et mattis ut, posuere at ligula. Nulla ultrices porttitor risus, sed aliquam nisl laoreet ut. Vestibulum sed dui sed velit lobortis luctus. Vestibulum facilisis nibh sit amet accumsan interdum. Donec ultrices imperdiet lectus ac ultricies. Maecenas lacinia nunc mi, quis eleifend lectus laoreet eu. Fusce a quam accumsan, feugiat ipsum tincidunt, elementum justo. Vivamus et imperdiet risus. Pellentesque quis viverra est. Phasellus sem mauris, fringilla ut convallis et, dapibus eget diam. Curabitur mattis arcu lacus, id finibus metus pellentesque eleifend. Suspendisse potenti. Proin tempor blandit nulla, hendrerit facilisis tortor fringilla sed. Fusce auctor lorem id neque porta accumsan. Nulla vulputate eu magna eu euismod.

Vestibulum eu justo ac elit fermentum porta. Cras in metus interdum, iaculis ante ac, pulvinar felis. Nullam feugiat blandit orci sed fringilla. Nulla nunc ipsum, sodales vel vulputate vitae, consequat quis elit. Integer non tortor vehicula felis pretium varius. Phasellus in tellus varius, sagittis nulla at, vehicula tortor. Nulla sed magna lorem. Praesent sit amet tellus non est aliquam tincidunt. Duis semper consequat eros, sit amet maximus ligula fringilla quis. Suspendisse potenti. Morbi tempus odio ac lorem cursus, vel sagittis lectus blandit. 
        ''',
        'banner':'img/Home.png',
        'nav':[
            ['/home','Home'],
            ['/about','About'],
            ['/blog','Blog'],
            ['/introduction','Introduction'],
            ['/music','Music'],
        ],
        'style':'css/styles.css',
        'author':'ilman teguh prasetya',
        'date': datetime.datetime.now(),
    }
    return render(request,'index.html',context)