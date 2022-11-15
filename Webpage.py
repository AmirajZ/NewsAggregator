from newspaper import Article
import webbrowser
url = 'https://timesofindia.indiatimes.com/city/srinagar/indias-goal-is-to-take-back-pok-turf-rajnath-singh/articleshow/95130709.cms'
url1 = 'https://www.aljazeera.com/news/2022/11/4/imran-khan-says-pakistan-pm-sharif-involved-in-plot-to-kill-him'
url2 = 'https://www.thehindu.com/news/international/russia-ukraine-conflict-has-widened-the-scope-of-political-leveraging-says-s-jaishankar/article66091243.ece'

'''India's news: Statement of Rajnath singh(MoD)'''

Articalpage = Article(url,language="en")
Articalpage.download()
Articalpage.parse()
Articalpage.title
Articalpage.text

'''News from Pakistan'''

Articalpage1 = Article(url1,language="en")
Articalpage1.download()
Articalpage1.parse()
Articalpage1.title
Articalpage1.text

'''News about Russia-Ukraine WAR'''

Articalpage2 = Article(url2,language="en")
Articalpage2.download()
Articalpage2.parse()
Articalpage2.title
Articalpage2.text

# print(Articalpage.title)
# print(Articalpage.text)

htmlpage = open("news.html","w")
htmldata= "<!DOCTYPE html><html lang='en'><head>    <meta http-equiv='X-UA-Compatible' content='IE=edge'>    <meta name='viewport' content='width=device-width, initial-scale=1.0'>    <title>Geopolitical News</title></head><body style='padding: 25x; color:black; border: 2px solid;'>    <div>        <H1 style='padding: 25x; color:black; border: 2px solid;'>"+Articalpage.title+"</H1> <P>"+Articalpage.text+"</P>   </div>     <div>        <H1 style='padding: 25x; color:black; border: 2px solid;'>"+Articalpage1.title+"</H1> <P>"+Articalpage1.text+"</P>   </div>   <div>        <H1 style='padding: 25x; color:black; border: 2px solid;'>"+Articalpage2.title+"</H1> <P>"+Articalpage2.text+"</P>   </div>  </body></html>"
htmlpage.write(htmldata)
htmlpage.close()

webbrowser.open("news.html")