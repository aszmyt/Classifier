Do testów gotowego klasyfiokatora wykorzystujemy plik ClassifyText.py i wymagamy pythona w wersji 3.5.x lub wyższej

Aby sklasyfikować zestaw testowy z plikami o ścieżkach postaci ./DIR/CATEGORY/FILE.txt
Podajemy przykładowo
python ClassifyText.py "./bbc"
Na wyjściu program poda jakość dopasowania opartą o przyporządkowanie do folderu z kategorią oraz listę dopasowań.

Do poprawnego działania programu wymagany jest pakiet nltk.
Najlepiej zainstalować pakiet Anaconda zapewniający wszystkie potrzebne biblioteki.

W celu wygenerowania nowego pliku ARFF należy uruchomić GenerateVector.py; 

W celu wytrenowania nowego klasyfikatora należy użyć skryptu Classifier.py

Załączony zbiór danych pozwala na uzyskanie sprawności klasyfikatora na poziomie 96%.