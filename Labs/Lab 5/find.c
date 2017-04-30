int find(char *key, int *p_ans){
	entry *e;
	int h;
	h = hash(key);

	for (e = table[h]; e!=NULL; e=e->next)
		if(strcmp(key, e->key) ==0)
		{
			*p_ands=e->val;
			return 1;
		}
	return 0;

}
