import re
import matplotlib.pyplot as plt
import numpy as np

regex = r"[a-zA-ZÀ-ÖØ-öø-ÿ]+"

stopwords = set([])
for s in open("stopwords-pt.txt", 'r').readlines():
    stopwords.add(s.strip().lower())

if __name__ == '__main__':

    file_name = ["feminismo.txt", "liberalismo.txt", "marxismo.txt"]

    for file in file_name:
        document = open(file, 'r')
        content = document.read()

        # identificacao de palavras
        words = re.findall(regex, content)
        frequencies = dict([])

        # quantidade de vezes no documento
        for w in words:
            w = w.lower()
            if w not in stopwords and len(w) > 2:
                if w not in frequencies:
                    frequencies[w] = 0
                frequencies[w] += 1


        # imprimir as 20 palavras mais frequentes
        fs = sorted(frequencies, key=frequencies.get, reverse=True)


        # GRÁFICO FREQUÊNCIAS
        x_axis = sorted(list(frequencies.values()), reverse=True)[:10]  # frequencias
        y_axis = sorted(frequencies, key=frequencies.get, reverse=True)[:10]  # palavras
        width = 0.75

        fig, ax = plt.subplots()
        plt.title('10 TERMOS MAIS FREQUENTES NO {}'.format(re.sub(r"\.txt", '', file).upper().strip()))
        plt.xlabel('NUMÉRO DE OCORRÊNCIAS')
        plt.ylabel('TERMOS')
        ind = np.arange(len(y_axis))
        ax.set_yticks(ind + width / 2)
        ax.set_yticklabels(x_axis, minor=False)
        ax.barh(y_axis, x_axis, width, align='center', color='black')

        for i, v in enumerate(y_axis):
            ax.text(v, i, " " + str(v), color='blak', fontweight='bold')

        plt.show()
        plt.savefig('palavras_frequentes_' + file.replace('.txt', '.png'))

