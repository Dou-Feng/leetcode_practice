#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int tot,l,t,op,ed,now;
    bool dp[1005],mk[600005];
    int e[600005][26],d[600005],to[600005],dep[600005],pos[10005];
    vector<string> ans;
    void add(string &s)
    {
        l=s.size(); t=1;
        for (int i=0;i<l;i++)
        {
            if (e[t][s[i]-'a']) t=e[t][s[i]-'a'];
            else t=e[t][s[i]-'a']=++tot;
            dep[t]=i+1;
        }
    }
    void bfs()
    {
        for (int i=0;i<26;i++) e[0][i]=1;
        to[1]=0;
        for (d[op=ed=1]=1;op<=ed;op++)
        {
            now=d[op];
            for (int i=0;i<26;i++)
            if (!e[now][i]) e[now][i]=e[to[now]][i];
            else to[d[++ed]=e[now][i]]=e[to[now]][i];
        }
    }
    bool hunt(string &s)
    {
        l=s.size(); t=1;
        if (!l) return false;//空串
        for (int i=1;i<=l;i++) dp[i]=false;
        for (int i=0;i<l;i++)
        {
            t=e[t][s[i]-'a'];
            for (now=t;now^1;now=to[now])//遍历fail祖先
            if (mk[now] && dp[i+1-dep[now]]) //是某个单词的末尾且之前的部分也可以由多个单词组成
            {
                dp[i+1]=true;
                break;
            }
        }
        return dp[l];
    }
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        int n=words.size();
        tot=1;
        for (int i=0;i<n;i++) 
        {
            add(words[i]);//建立tire树
            mk[pos[i]=t]=true;//标记
            pos[i]=t;
        }
        bfs();//跑fail数组
        dp[0]=true;
        for (int i=0;i<n;i++)
        {
            mk[pos[i]]=false;//取消标记
            if (hunt(words[i])) ans.push_back(words[i]);
            mk[pos[i]]=true;//恢复标记
        }
        return ans;
    }
};
