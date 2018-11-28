import csv
from textblob import TextBlob

with open('data.csv', 'rt', encoding='utf-8', newline='') as csvfile:

    with open('data_analysis.csv', 'a') as an:
        reader = csv.DictReader(csvfile)
        writer = csv.writer(an)
        writer.writerow(["datetime", "polarity", "subjectivity"])
        polcount = 0.0
        subcount = 0.0
        counter = 0
        poltab = []
        subtab = []
        for row in reader:
            tweet = row['text']
            created = row['created_at']
            analysis = TextBlob(tweet)
            writer = csv.writer(an)
            writer.writerow([created, analysis.sentiment.polarity, analysis.sentiment.subjectivity])
            poltab.append(analysis.sentiment.polarity)
            subtab.append(analysis.sentiment.subjectivity)
            polcount = polcount + analysis.sentiment.polarity
            subcount = subcount + analysis.sentiment.subjectivity
            counter = counter +1

        avgp=polcount/counter
        avgs=subcount/counter
        print('Avg polarity:', avgp)
        print('Avg subjectivity:', avgs)