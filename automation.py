beforeHtml="<html><body><script src='https://cdn.jsdelivr.net/clipboard.js/1.5.3/clipboard.min.js'></script><table style='border: 1px solid black'>"
afterHtml="</table><script> var clipboard = new Clipboard('.copyButton'); clipboard.on('success', function(e) { console.log(e);}); clipboard.on('error', function(e) {    console.log(e);}); </script></body></html>"
pattern="<tr><td style='border: 1px solid black' id='{0}' value='{1}'>{1}</td><td style='border: 1px solid black'><button class='copyButton' id='copyButtonId' data-id='@item.Type' data-clipboard-action='copy' data-clipboard-target='#{0}'>Copy!</button></td></tr>"
inputFile = open("testcase.txt","r")
outputFile = open("output.html", "w")
html=beforeHtml
id=0
lines = inputFile.readlines()
for line in lines:
    html+=pattern.format("id" + str(id), line)
    id=id+1
html+=afterHtml
outputFile.write(html)
outputFile.close()
inputFile.close()
