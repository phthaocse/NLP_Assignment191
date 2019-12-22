from Models import *

def write_data(file_output,data):
    f = open(file_output, 'w+')
    n = len(data)
    k = len(data[0])
    for i in range(n):
        f.write(str(data[i])+'\n')
    f.close()
    return True

#Read question from input file
quest_list = []
with open(r"Input/questions.txt") as questions:
    for question in questions:
        quest_list += [question.strip('\n')]

a_output = [[],[]]
b_output = [[],[]]
c_output = [[],[]]
d_output = []

#Preprocess phase: tokenize -> pos tagging -> dependency parser 
for question in quest_list:
    toknenize_obj = tokenlizer.Tokenizer()
    token = toknenize_obj.tokenize(question)
    word_list = toknenize_obj.finalTokenize(token)
    postag = pos_tagging.PosTag(word_list)
    pos_tag_res = postag.tagging()
    #arc-eagers parsing
    dependency_gram = arceager_parser.ArcEagerParser(pos_tag_res)
    dependency_gram.parsing()
    #covert to grammatical relation
    gram_relation = gramRelation.GrammaticalRelation(dependency_gram.relation)
    a_output[0] += [question]
    tmp = gram_relation.convertFromDep() 
    a_output[0] += tmp[0]
    a_output[1] += [tmp[1]]
#write data for problem a
write_data('Output/output_a.txt',a_output[0])

#Problem b: Create logical form 
tmp_print = []
for item in a_output[1]:
    log_form = logicalform.LogicalForm(item)
    log_form.get_logical_form()
    b_output[0] += [log_form.print_logic_form()]
    b_output[1] += [log_form.logic_form]
# print(b_output)
for i in range(len(quest_list)):
    tmp_print += [quest_list[i]] + [b_output[0][i]]

# print(tmp_print)
#write data for problem b
write_data('Output/output_b.txt',tmp_print)

#Problem c: Create procedual sematic
tmp_print = []
for ele in b_output[1]:
    procedual = proce_sem.ProceudalSematic(ele)
    c_output[1] += [procedual.get_proc_sem()]
    c_output[0] += [procedual.print_sem()]
# print(c_output)
for i in range(len(quest_list)):
    tmp_print += [quest_list[i]] + [c_output[0][i]]

write_data('Output/output_c.txt',tmp_print)

#Problem d: Query DB to find answer
tmp_print = []
for proc in c_output[1]:
    ans_query = query.Query(proc)
    ans = ans_query.get_answer()
    d_output += [ans[1]]

for i in range(len(quest_list)):
    tmp_print += [quest_list[i]] + [d_output[i]]

write_data('Output/output_d.txt',tmp_print)