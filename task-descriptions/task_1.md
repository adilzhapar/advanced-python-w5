## Task 1 - Extracting Information from HTML Page
___

### Goal
> There are `.html` files with data in `contractspecfs` directory.  
> You need to determine whether specific texts are present on the .html pages or not.    
> Calculate the frequency (how often each text occurred) and write the result to a `json` file with name `task_1_result.json`.  

<br>

### Texts and What to Look For
Between each word in the text, there may be **any amount** of spaces and tab characters.   
The texts `банковская гарантия на сумму аванса по договору` and `банковская гарантия                         на сумму аванса по договору` are considered the same.

> 1. A - No Security for Contract Performance
> 2. B - Guarantee cash deposit of 3% of the total contract amount
> 3. C - Bank guarantee in the amount according to Article 26 of the Law
> 4. D - Cash guarantee deposit in the amount according to Article 26 of the Law
> 5. E - Collateral with money from an electronic wallet of 3% of the total contract amount
> 6. F - Collateral with money from an electronic wallet in the amount according to Article 26 of the Law
> 7. G - Bank guarantee for the advance amount under the contract
> 8. H - Civil liability insurance contract for 3% of the total contract amount
> 9. I - Bank guarantee for 3% of the total contract amount

<br>

### Expected Result
> File `task_1_result.json` with the following structure

```json
{
    "absenceSecurityPerformanceContract": <number of occurrences of text A>,
    "securityDepositTotalAmountContract": <number of occurrences of text B>,
    "bankGuaranteeAmountInAccordanceLaw26": <number of occurrences of text C>,
    "cashGuaranteeAmountInAccordanceLaw26": <number of occurrences of text D>,
    "ewalletCollateralMoney3percentContractAmount": <number of occurrences of text E>,
    "ewalletMoneyAmountInAccordanceLaw26": <number of occurrences of text F>,
    "bankGuaranteeAmountInAdvanceUnderContract": <number of occurrences of text G>,
    "civilLiabilityInsurance3percentTotalContractAmount": <number of occurrences of text H>,
    "bankGuarantee3percentTotalContractAmount": <number of occurrences of text I>
}
```

<br>





