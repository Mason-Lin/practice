# SOP

1. 非常仔細聽問題的所有描述
2. 給一個適當大小的範例
3. 提出一個暴力的解決辦法，講解演算法並分析執行時間
4. 對暴力解法進行優化，檢查未使用到的資訊，提出更好的解法
5. 仔細檢查解法，確保沒有錯誤
6. 實作漂亮的程式碼，並寫大聲思考
7. 測試，確保沒有錯誤

https://leetcode.com/explore/interview/card/cheatsheets/720/resources/4725/

# 第一階段：介紹

準備好 30-60 秒的關於您的教育背景、工作經驗和興趣的介紹。
微笑並充滿自信地說話。
當面試官談論他們自己時要注意，稍後將他們的工作納入你的問題中。

# 第二階段：問題陳述 (搞清楚題目)

當面試官讀給你聽後，**將問題複述給他們聽**。
詢問有關輸入的**澄清問題**，例如預期輸入大小、邊緣情況和無效輸入。
快速瀏覽範例測試案例以確認您瞭解問題。
I have read and understood the problem, but I have some clarification questions, and could we discuss them?
Anything I can know about the range of these values?
Can you tell me the size of the array?
What is the maximum possible number in this array?
Is this understanding correct?

# 第三階段：腦力激盪 DS&A (討論可能的解法, 分析並總結所有解法)

始終大聲地思考。
將問題分解：弄清楚你需要做什麼，並思考什麼資料結構或演算法可以以良好的時間複雜度完成它。
接受面試官的任何評論或回饋，他們可能試圖暗示你找到正確的解決方案。
一旦你有了一個想法，**在編碼之前，向面試官解釋你的想法**，並確保他們理解並同意這是一個合理的方法。
Of course you are not looking for this brute force implementation, this can be optimized by..

# 第四階段：實施 (寫程式)

在實施時解釋您的決策。當你聲明像 collections 這樣的東西時，解釋一下目的是什麼。
編寫符合您的程式語言約定的乾淨程式碼。
避免編寫重複的程式碼 - 如果多次編寫類似的程式碼，請使用輔助函數或 for 迴圈。
**如果您陷入困境，請不要驚慌** - 與面試官溝通您的疑慮。
**不要害怕從暴力解決方案開始**（同時承認它是暴力），然後透過優化「慢」部分來改進它。
繼續大聲思考並與面試官交談。這使他們更容易給您提示。
should I start implement it in code or you want me to continue to optimize it?
//check null, May I skip these checks to save time?
May I keep the variable names short just for convenience when coding in google doc? In real code I will use more descriptive names

# 第五階段：測試和調試 (主動檢查與測試)

當遍歷測試用例時，透過在**文件底部寫入來追蹤變量，並不斷更新它們**。壓縮瑣碎的部分，例如創建前綴和以節省時間。
如果發生錯誤且環境支援運行程式碼，請將列印語句放入您的演算法中並遍歷一個小測試案例，比較變數的預期值和實際值。
**如果遇到任何問題，請直言不諱並繼續與面試官交談。**

# 第六階段：解釋和跟進 (複雜度分析)

您應該準備回答的問題：

**時間和空間複雜度、平均情況和最壞情況。**
**為什麼選擇這個資料結構、演算法或邏輯？**
您認為該演算法在複雜性方面**是否可以改進？**如果他們問你這個問題，那麼**答案通常是肯定的**
特別是如果你的演算法比 O(n)慢的時候

# 第七階段：尾聲

**準備好有關公司的問題。**
**對面試官的回答表現出興趣、微笑並提出後續問題。**
