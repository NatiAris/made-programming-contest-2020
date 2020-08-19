def process_tag(stack, tag, fail_count, strategy):
    if fail_count > 1:
        return None
    if tag[0] != '/':  # Opening tag, add to stack
        stack.append(tag)
        return None
    if len(stack) == 0:  # Closing tag + empty stack
        # Two options:
        # - remove last item from stack and try again
        # - ignore this item
        # but in this case, we can only ignore
        if strategy == 'left':
            return -1
        return tag
    if stack[-1] == tag[1:]:  # Correct closing tag
        stack.pop()
        return None
    # Incorrect closing tag
    if fail_count == 0:  # Recoverable
        if strategy == 'left':
            removed_elem = stack.pop()
            process_tag(stack, tag, fail_count + 1, strategy)
            return removed_elem
        else:
            removed_elem = tag
            return removed_elem
    if fail_count == 1:  # Irrecoverable
        return -1

def solve(tags, strategy='left'):
    stack = []
    fail_count = 0
    tag_to_remove = None
    
    for tag in tags:
        if fail_count > 1:
            break
        maybe_tag = process_tag(stack, tag, fail_count, strategy)
        if maybe_tag is not None:
            if maybe_tag == -1:
                fail_count += 10
            tag_to_remove = maybe_tag
            fail_count += 1
    
    # print(stack, tag_to_remove)
    result = 'CORRECT'
    if stack:
        if len(stack) == 1 and tag_to_remove is None:
            result = 'ALMOST <' + stack[0] + '>'
        else:
            result = 'INCORRECT'
    elif fail_count == 1:
        result = 'ALMOST <' + tag_to_remove + '>'
    elif fail_count > 1:
        result = 'INCORRECT'
    if result == 'INCORRECT' and strategy == 'left':
        result = solve(tags, strategy = 'right')
    return result


T = int(input().strip())
for _ in range(T):
    h = int(input().strip())
    tags = [input().strip()[1:-1].upper() for _ in range(h)]
    print(solve(tags))
