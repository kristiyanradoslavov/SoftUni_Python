from collections import deque

eggs = deque(map(int, input().split(", ")))
papers = deque(map(int, input().split(", ")))
box_size = 50

boxes_count = 0

while eggs:
    if not papers:
        break

    if eggs[0] <= 0:
        eggs.popleft()
        continue
    elif eggs[0] == 13:
        eggs.popleft()
        papers_first = papers.popleft()
        papers_last = papers.pop()
        papers.append(papers_first)
        papers.appendleft(papers_last)
        continue

    if eggs[0] + papers[-1] > box_size:
        eggs.popleft()
        papers.pop()

    elif eggs[0] + papers[-1] <= box_size:
        eggs.popleft()
        papers.pop()
        boxes_count += 1

if boxes_count >= 1:
    print(f"Great! You filled {boxes_count} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")

if papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")