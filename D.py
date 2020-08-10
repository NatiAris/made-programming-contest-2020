def almost(tag):
    return 'ALMOST <' + tag + '>'

def inverse_tag(tag):
    if type(tag) is not str:
        return tag
    if tag[0] == '/':
        return tag[1:]
    else:
        return '/' + tag

def process_tag(stack, tag, fail_count):
    if fail_count > 1:
        return -1
    if tag[0] != '/':  # Opening tag, add to stack
        stack.append(tag)
        return None
    if len(stack) == 0:  # Closing tag + empty stack
        if fail_count == 0:  # Recoverable
            return tag
        else:
            return -1  # Irrecoverable
    if stack[-1] == tag[1:]:  # Correct closing tag
        stack.pop()
        return None
    # Incorrect closing tag
    if fail_count == 0:  # Recoverable
        return tag
    if fail_count == 1:  # Irrecoverable
        return -1

def process_tags(tags):
    stack = []
    fail_count = 0
    tag_to_remove = None
    
    for tag in tags:
        if fail_count > 1:
            break
        maybe_tag = process_tag(stack, tag, fail_count)
        if maybe_tag is not None:
            if maybe_tag == -1:
                fail_count += 1
                break
            else:
                tag_to_remove = maybe_tag
                fail_count += 1
    
    # print(stack, tag_to_remove, fail_count)
    if fail_count == 0 and len(stack) == 0:
        return True
    if fail_count == 0 and len(stack) == 1:
        return stack[0]
    if fail_count == 1 and len(stack) == 0:
        return tag_to_remove
    return False
    

def solve(tags):
    right_result = process_tags(tags)
    inversed_tags = [inverse_tag(tag) for tag in reversed(tags)]
    left_result = inverse_tag(process_tags(inversed_tags))
    
    if left_result == right_result == True:
        return 'CORRECT'
    if left_result == right_result == False:
        return 'INCORRECT'
    if left_result == False:
        return almost(right_result)
    if right_result == False:
        return almost(left_result)
    if left_result == right_result:
        return almost(left_result)
    raise Exception(left_result, right_result)


T = int(input().strip())
for _ in range(T):
    h = int(input().strip())
    tags = [input().strip()[1:-1].upper() for _ in range(h)]
    print(solve(tags))
