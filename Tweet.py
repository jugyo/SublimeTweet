import sublime_plugin
import subprocess
import urllib

class TweetCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        texts = []
        for region in self.view.sel():
            texts.append(self.view.substr(region))
        text = ' '.join(texts)
        text = text.encode('utf-8')
        text = urllib.quote(text)
        url = 'https://twitter.com/intent/tweet?text=%s' % text
        subprocess.call(["open", url])
