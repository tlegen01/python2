text1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eu magna sit amet neque lobortis dignissim. " \
        "Mauris vehicula lacinia bibendum. Phasellus elementum ipsum et mi mollis, sed eleifend elit pharetra. " \
        "Donec interdum tempus ligula non vulputate. Cras mollis rhoncus facilisis. Fusce at viverra magna, id tempor " \
        "nulla. Quisque at felis eget arcu gravida efficitur eget ac enim. Etiam quisque efficitur lorem at lorem " \
        "dictum, a sagittis ipsum pulvinar. Maecenas elit nisi, iaculis a dolor id, tempor molestie dolor. Pellentesque" \
        " aliquet non orci at convallis. Donec laoreet nisl quam. Ut accumsan, dui ut mattis ultricies, est nulla semper" \
        " est, eget pulvinar magna lacus ut risus. " \
        "Duis sed hendrerit odio. Etiam scelerisque nunc quis placerat interdum. Nam condimentum enim ac justo " \
        "fermentum, et imperdiet purus finibus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Mauris " \
        "bibendum urna vitae ullamcorper pellentesque. Aenean in est vitae felis semper vulputate convallis eu quam. " \
        "Nullam feugiat elementum libero. Donec scelerisque finibus laoreet. Nam eu risus facilisis, iaculis urna vitae," \
        " aliquam neque. Donec elementum ipsum in pretium maximus. " \
        "Integer id nulla commodo elit ultricies sollicitudin vel vitae augue. Proin commodo, magna at bibendum rutrum, " \
        "odio risus dictum nisi, ac commodo ipsum dolor vitae purus. Maecenas posuere, est id vulputate porta, erat" \
        " lacus efficitur purus, a mattis justo ligula eu felis. Suspendisse potenti. Mauris commodo libero ut dui" \
        " efficitur malesuada. Donec ultricies vel purus vel pellentesque. Etiam fusce a ex in libero rutrum placerat" \
        " suscipit ac tellus. Etiam dignissim ullamcorper tincidunt. Proin tempor lorem eu nulla euismod, id" \
        " sollicitudin massa ultricies."

text2 = text1.lower()
str1 = "etiam"
find1 = text2.find(str1)
find2 = text2.find(str1, 386)
find3 = text2.find(str1, 713)
find4 = text2.find(str1, 1563)
arr1 = [x for x in str1]

index = 0
for i in arr1:
        print(ord(i))

arr1.sort(reverse=True)
print(arr1)