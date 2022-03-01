import bibtexparser
from bibtexparser.bparser import BibTexParser
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from datetime import datetime
import matplotlib.colors
import dateutil

color_palett = ["#274060","#239f91","#335c81","#65afff"]
color_palett_rgab = [matplotlib.colors.to_rgb(c) for c in color_palett]

def pieChartOfUniqueReferenceTypes(bibtex_entries,filepath):
    # Filter and Count unique types of references 
    cit_typs = list([ref["ENTRYTYPE"] for ref in bibtex_entries])
    cit_count = Counter(cit_typs)

    # Construct a pie chart out of the different types
    values = [x for l, x in cit_count.items()]
    labels = [l for l, x in cit_count.items()]
    plt.pie(values, labels=labels,autopct='%1.1f%%',colors=color_palett_rgab)

    # saves into libary folder
    plt.savefig(filepath)

    print("Wrote pie chart png to output dir")

def wordcloudOfBibtexTags(bibtex_entries,filepath):
    # extract keywords out of bibtex database
    keywords = []
    for ref in bibtex_entries:
        if 'keywords' in ref:
            keywords.extend([word for word in ref['keywords'].split(",") if word != "used"])

    # construct the wordcloud
    wordcloud = WordCloud(width=1600, height=800,background_color="white").generate(" ".join(keywords))

    # matploblib options for higher resolution
    plt.figure( figsize=(20,10), facecolor='k')
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(filepath,facecolor='k', bbox_inches='tight')

    print("Wrote Wordcloud png to output dir")

def findTimeSpanOfPapers(bibtex_entries):
    dates = list([dateutil.parser.parse(ref['date']) for ref in bibtex_entries if 'date' in ref])
    dates = sorted(dates)
    min_years = ",".join([str(date.year) for date in dates[:2]])
    max_years = ",".join([str(date.year) for date in dates[-2:]])

    print(f"References are in the time range of {min_years} to {max_years}")


# Parses the bibtex file o the project
with open("literatur/literatur.bib") as bibtex_file:
    from bibtexparser.bparser import BibTexParser

    parser = BibTexParser()
    parser.ignore_nonstandard_types = False
    parser.homogenize_fields = False
    parser.common_strings = False
    bib_database = bibtexparser.load(bibtex_file, parser)

print(f"Found {len(bib_database.entries)} entries in the biblography file.")
findTimeSpanOfPapers(bib_database.entries)

# Draw the unique types of Graphs
pieChartOfUniqueReferenceTypes(bib_database.entries,"literatur/cit_count_bar_chart.png")
wordcloudOfBibtexTags(bib_database.entries,"literatur/cit_wordcloud_tags.png")