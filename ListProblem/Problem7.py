# def sortlist(a):
#     a= [i for i in range(len(a)-1) if a[i+1]> a[i]] or [i for i in  range(len(a)-1) if a[i] > a[i+1]]
#     print("List is not sorted.")
#     return
#     print("Sorted list")
# newlist= [50, -30, 70, 190, -500, 200]
# sortlist(newlist)

def is_sorted(a):
    i = 0
    asc_ok = True   # ascending ধরে শুরু করি
    desc_ok = True  # descending ধরে শুরু করি

    while i < len(a) - 1:
        if a[i] > a[i+1]:   # এখানে বড় → ascending ভাঙলো
            asc_ok = False
        if a[i] < a[i+1]:   # এখানে ছোট → descending ভাঙলো
            desc_ok = False
        i = i + 1

    if asc_ok:
        print("Ascending sorted ✅ (ছোট → বড়)")
    elif desc_ok:
        print("Descending sorted ✅ (বড় → ছোট)")
    else:
        print("NOT sorted ❌")

# Test করো:
# newlist1 = [50, -30, 70, 190, -500, 200]
newlist2 = [-500, -30, 50, 70, 190, 200]
# newlist3 = [200, 190, 70, 50, -30, -500]

# is_sorted(newlist1)  # → NOT sorted ❌
is_sorted(newlist2)  # → Ascending sorted ✅
# is_sorted(newlist3)  # → Descending sorted ✅