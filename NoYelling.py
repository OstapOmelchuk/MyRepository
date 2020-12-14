def filter_words(st):
    st = st[0].upper() + st[1:].lower()
    st = " ".join(st.strip().split())
    return st