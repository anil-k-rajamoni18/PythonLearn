'''
nested if
- writing if & else block inside another if & else block
'''
age = int(input('Enter age: '))
have_voter_id = input('Do you have VoterId Yes | No?:  ').lower()
have_voter_id = True if have_voter_id == 'yes' else False  #short hand if else

if age >= 18: # outer if block
    if have_voter_id: # inner if lock
        print('eligible to cast vote')
    else:
        print('please apply voter id')
else:
    print('not eligible to cast vote')