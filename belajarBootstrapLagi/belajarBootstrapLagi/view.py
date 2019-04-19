from django.shortcuts import render
import datetime
def index(request):
    context={
        'title':'Home',
        'heading':'Welcome',
        'author':'ilman',
        'banner':'img/Home.png',
        'date':datetime.datetime.now,
        'logo':'img/logo_transparent.png',
        'article':'''
            Lorem ipsum dolor sit amet, in utinam aliquip maiestatis mel. Id enim augue nec, has et atqui mazim luptatum. Pro eu primis voluptua delectus, dico omnes laboramus vix ei. Ius ne saepe ridens, nihil principes et eos. Wisi electram inciderint eu vix. Eu dicta vivendo prodesset ius, ex unum summo adipisci eos.

            Reque soleat usu te. Mel id sale illud graecis. Duis probo putant cu qui, mea ex nonumes omnesque neglegentur. Debitis minimum offendit at has. Te mei etiam partiendo, est ne quodsi denique inciderint, eros pertinax interpretaris mel ei. Nec ei appareat aliquando necessitatibus, mel laudem offendit scripserit in.

            Mel atqui oratio urbanitas ei, nec libris vulputate ad, qui tantas cetero definitionem id. Modo putant aliquando ut sea, pro idque dicam vivendum ei. Nulla munere feugait qui ut. Ornatus maluisset mei eu, ut sed facete pertinax. Eu mei accusam invenire.

            Nam diceret recteque neglegentur cu, id nam intellegam referrentur. Usu insolens salutatus dissentias ne, vix iriure nusquam fierent in. Eu qui liber exerci assentior, in oblique consulatu per. Eum at altera vulputate, partem quidam ei ius, oratio mandamus principes at sit.

            Ex est rebum malis dissentias, ex vis solum albucius voluptaria, facer constituto liberavisse has no. Cu sit diam postea noluisse, elitr dolorum temporibus duo cu. An omnesque explicari mel, ex sea feugiat omnesque democritum. Id dicat decore vim, vim dicam efficiendi conclusionemque an, ad mea dicta partem. Cu mucius patrioque nec.
        ''',
        'nav':[
            ['/home','Home'],
            ['/music', 'Music'],
            ['/blog','Blog'],
            ['/about','About'],
        ]
    }
    return render(request,'index.html',context)