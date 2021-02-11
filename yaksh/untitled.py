
def halo(justdict):
    nan = ''
    # questions = []
    

    #justdict = {0: {'summary': 'Choose the correct answer 1', 'type': 'mcq', 'language': 'other', 'description': '<p>Trial Question 1</p>', 'points': 1, 'testcase.0.test_case_type': 'mcqtestcase', 'testcase.0.options': 'Option 1', 'testcase.0.correct': 0, 'testcase.1.test_case_type': 'mcqtestcase', 'testcase.1.options': 'Option 2', 'testcase.1.correct': 1, 'testcase.2.test_case_type': 'mcqtestcase', 'testcase.2.options': 'Option 3', 'testcase.2.correct': 0, 'testcase.3.test_case_type': 'mcqtestcase', 'testcase.3.options': 'Option 4', 'testcase.3.correct': 0, 'active': 1, 'grade_assignment_upload': 0, 'min_time': 0, 'partial_grading': 0, 'snippet': nan, 'solution': nan, 'tags.0': 'tag2', 'tags.1': 'tag1', 'topic': 'Topic Name'}, 1: {'summary': 'Choose the correct answer 2', 'type': 'mcq', 'language': 'other', 'description': '<p>Trial Question 2</p>', 'points': 2, 'testcase.0.test_case_type': 'mcqtestcase', 'testcase.0.options': 'Option 2', 'testcase.0.correct': 0, 'testcase.1.test_case_type': 'mcqtestcase', 'testcase.1.options': 'Option 3', 'testcase.1.correct': 0, 'testcase.2.test_case_type': 'mcqtestcase', 'testcase.2.options': 'Option 4', 'testcase.2.correct': 1, 'testcase.3.test_case_type': 'mcqtestcase', 'testcase.3.options': 'Option 5', 'testcase.3.correct': 0, 'active': 1, 'grade_assignment_upload': 0, 'min_time': 0, 'partial_grading': 0, 'snippet': nan, 'solution': nan, 'tags.0': 'tag3', 'tags.1': 'tag2', 'topic': 'Topic Namex'}}

    def get_opt_list():
        for i in mdict:
            if i.startswith('testcase') and i.endswith('options'):
                yield {'options':mdict[i]}
            elif i.startswith('testcase') and i.endswith('correct'):
                if mdict[i] == 1:
                    res = True
                if mdict[i] == 0:
                    res = False
                yield {'correct':res}
            elif i.startswith('testcase') and i.endswith('test_case_type'):
                yield {'test_case_type':mdict[i]}


    for i in justdict:
        opt_dict = {}
        mdict = justdict[i]

        tags_list = []
        for i in mdict:
            if i.startswith('tags'):
                tags_list.append(mdict[i])

        a = get_opt_list()
        o_list = []
        o_dict = {}
        for i in a:
            for key in i.keys():
                if key != 'correct':
                    o_dict.update(i)
                else:
                    o_dict.update(i)
                    o_list.append(o_dict)
                    o_dict = {}
        # print(o_dict)


        # print(o_list)

        for i in mdict:
            if i.startswith('testcase') and 'test_case' not in [key  for key in opt_dict.keys()]:
                opt_dict.update({'testcase':o_list})
            elif i.startswith('tags'):
                opt_dict.update({'tags':tags_list})
            else:
                opt_dict.update({i:mdict[i]})

        yield opt_dict

# r = halo()
# for i in r:
#     print(i)