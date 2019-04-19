from django.shortcuts import render
import datetime
def index(request):
    context={
        'title':'Home',
        'quotes':'''
            I believe in the religion of Islam. I believe in Allah and peace
        ''',
        'scrolling':'js/scrolling.js',
        'auhtorQuotes':'Muhammad Ali',
        'headingArticle':'Selamat Datang',
        'author':'ilman teguh prasetya',
        'date':datetime.datetime.now(),
        'icon':'img/favicon.png',
        'gambarLogo':'img/logo.png',
        'tool':[
            ['/menu', 'Menu'],
            ['/menu', 'Menu'],
            ['/menu', 'Menu'],
            ['/menu', 'Menu'],
        ],
        'pooper':'vendor/bootstrap/js/popper.min.js',
        'jquery':'vendor/bootstrap/js/jquery.js',
        'bootstrapJs':'vendor/bootstrap/js/bootstrap.min.js',
        'bootstrapCss':'vendor/bootstrap/css/bootstrap.min.css',
        'cssCustom':'css/styles.css',
        'article':'''
            Lorem ipsum dolor sit amet, euripidis voluptatum ne cum. In euismod omittam officiis mei, est no dico copiosae sapientem. Denique neglegentur in vix. Ut eos libris principes. Omnis praesent eu cum, vix ea porro legendos intellegam, quem iudicabit vix ei.
            
            Quis mucius accommodare his an, an vix accusamus consequat concludaturque, aeterno nonumes ius ea. Mel id option consequuntur definitiones. Ex equidem vivendo eos, ut nec utroque philosophia, ludus dicam oratio eu pro. Ius gubergren intellegam reformidans te, at expetenda comprehensam nam. Aliquam deleniti ex vis, dolor ancillae copiosae est eu. Sed no legendos scribentur, vix in reque etiam soluta, mei te simul probatus.
            
            Dolores percipitur sea ne. Et dolores definitiones vim, cum ex legendos voluptatibus, soleat recteque instructior an mel. Et pro nibh eruditi vivendum, stet prompta splendide mei an, quem eruditi eam ut. Mel liber interpretaris at, cum possit ponderum expetendis te, noster iriure scribentur no has.
            
            Omnes putent conceptam est ne. Usu ne audire commodo accusata, euismod explicari vulputate nec ea. Usu eu saepe quodsi, ex phaedrum nominati pro, ei graece instructior vel. Eam ullum placerat intellegam cu, purto malis patrioque cu mei.
            
            At diam apeirian vis, eum vide reprimique ea. Ius ei facer ponderum, quo te erat dicam tibique. Quo at velit fastidii detraxit. Rebum augue omnesque te nam. Eu eum simul congue quidam, mel te natum quodsi placerat.
        ''',
    }
    return render(request,'index.html',context)