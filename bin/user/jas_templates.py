#    Copyright (c) 2026 Rich Bell <bellrichm@gmail.com>
#
#    See the file LICENSE.txt for your full rights.
#

'''
Data templates used by JAS skin.
'''

data_load_template = \
'''<!doctype html>
<html>
  <head>
    <meta name="generator" content="jas {VERSION} {gen_time}">
    <script src="https://cdn.jsdelivr.net/npm/moment@{momentjs_version}/moment{momentjs_minified}.js"></script>
{script_string}    <script>
      window.addEventListener("load", function (event) {{
      console.debug(Date.now().toString() + " iframe start");
{dataload_string}        message = {{}};
        message.kind = "dataLoaded";
        message.message = JSON.stringify(pageData);
        window.parent.postMessage(message, "*");
        console.debug(Date.now().toString() + " iframe end");
      }})
    </script>
  </head>
</html>
'''

data_load_template2 =\
'''// the start
'''

data_load_template2 +=\
'''/* jas {VERSION} {gen_time} */
'''
