# Metriken 

Im Folgenden wird meine iOS-App [Stirnraten](https://stirnraten.de/softwaretechnik/deployment_diagram.html) untersucht auf
- Lines of Code
- Testabdeckung
- Finden von unbenutzten Code
- ... 

## Testabdeckung

Verwendetes Tool: [XCov](https://github.com/nakiostudio/xcov). Dieses Tool wertet die Logs, die nach einem Projekt-Test erstellt werden aus und stellt die Coverage grafisch dar. Siehe hier. 



## Lines of Code

Lines of Code  `4954`  Wobei es klassischerweise schwierig ist, zu beurteilen, was diese Zahl aussagt. 🤷‍♂️
Ein Swift-Linter sagt, dass eine *.swift nicht länger als 400 Zeilen sein sollte. Dies trifft auf alle Files zu.
Ein weiterer Richtwert ist, dass in einem Swift-ViewController nicht mehr als 175 Zeilen haben sollte. 

Bis auf den RungameViewController sind alle ViewController in diesem Limit. 
```288 ./ViewControllers/ViewController/Main/RunGameViewController/RunGameViewController.swift```  
Bei einer Analyse ergab sich, dass der RungameViewController tatsächlich unsauber entwickelt ist und an einigen Stellen das MVC Pattern verletzt, da zu viel Spiellogik im View liegt. Ich habe mir ein Ticket erstellt.  

Shell Command for Lines Of Code
```find . -path ./Pods -prune -o -name "*.swift" -print0 ! -name "/Pods" | xargs -0 wc -l```

Result
```
28 ./Xibs/RatingView.swift
28 ./Xibs/ForwardingView.swift
25 ./ViewController.swift
78 ./Tools/General.swift
105 ./Tools/PurchaseTool.swift
45 ./Tools/Rating.swift
379 ./Tools/Alerts/AlertmachinePresenter.swift
13 ./Tools/Alerts/AlertTypes.swift
138 ./Tools/Alerts/Alertmachine.swift
13 ./Tools/Alerts/PersistenceKeys.swift
36 ./Tools/Alerts.swift
166 ./Tools/Layouter.swift
97 ./Tools/AnimationTool.swift
25 ./Tools/DateTool.swift
119 ./Tools/PersistenceTool.swift
79 ./Tools/SoundTool.swift
26 ./Categories.swift
19 ./Extensions/UIImageViewExtension.swift
80 ./Extensions/DeviceExtensions.swift
21 ./Extensions/BundleExtensions.swift
15 ./Extensions/DateExtension.swift
15 ./ViewControllers/BaseViewController/BaseNavigationViewController.swift
86 ./ViewControllers/BaseViewController/StirnratenBaseViewController.swift
38 ./ViewControllers/ViewController/Settings/PageViewControllers/StepViewController.swift
54 ./ViewControllers/ViewController/Settings/PageViewControllers/HelpPageViewController.swift
81 ./ViewControllers/ViewController/Settings/PageViewControllers/HelpPageViewController+UIPageDataSource.swift
104 ./ViewControllers/ViewController/Settings/ThemeViewController/ThemeViewController+TableView.swift
17 ./ViewControllers/ViewController/Settings/ThemeViewController/ThemesViewController+ButtonAction.swift
37 ./ViewControllers/ViewController/Settings/ThemeViewController/ThemesViewController.swift
28 ./ViewControllers/ViewController/Settings/SettingsViewController/SettingsViewController+ButtonAction.swift
177 ./ViewControllers/ViewController/Settings/SettingsViewController/SettingsViewController.swift
148 ./ViewControllers/ViewController/Shop/ShopViewController/ShopViewController+TableView.swift
71 ./ViewControllers/ViewController/Shop/ShopViewController/ShopViewController.swift
86 ./ViewControllers/ViewController/Main/RandomViewController/RandomViewController.swift
50 ./ViewControllers/ViewController/Main/RandomViewController/RandomViewController+PanGesture.swift
16 ./ViewControllers/ViewController/Main/RandomViewController/RandomViewController+ButtonAction.swift
147 ./ViewControllers/ViewController/Main/RandomViewController/RandomViewController+CollectionView.swift
22 ./ViewControllers/ViewController/Main/PremiumViewController/PremiumViewController+ButtonAction.swift
136 ./ViewControllers/ViewController/Main/PremiumViewController/PremiumViewController.swift
121 ./ViewControllers/ViewController/Main/FinishViewController/FinishViewController.swift
16 ./ViewControllers/ViewController/Main/FinishViewController/FinishViewController+MailDelegate.swift
22 ./ViewControllers/ViewController/Main/FinishViewController/FinishViewController+ButtonAction.swift
46 ./ViewControllers/ViewController/Main/FinishViewController/FinishViewController+TableView.swift
23 ./ViewControllers/ViewController/Main/FinishViewController/FinishedViewController+Cheers.swift
32 ./ViewControllers/ViewController/Main/RunGameViewController/RunGameViewController+ButtonActions.swift
288 ./ViewControllers/ViewController/Main/RunGameViewController/RunGameViewController.swift
71 ./ViewControllers/ViewController/Main/CategoriesViewController/CategoriesViewController.swift
159 ./ViewControllers/ViewController/Main/CategoriesViewController/CategoriesViewController+CollectionView.swift
15 ./ViewControllers/ViewController/Main/RunGameNavigationController/RunGameNavigationController.swift
41 ./ViewControllers/ViewController/Main/PermissionViewController/PermissionViewController.swift
77 ./ViewControllers/ViewController/Main/StartVIewController/StartViewController.swift
40 ./ViewControllers/ViewController/Imprint/LicensesViewController/LicensesViewController.swift
39 ./ViewControllers/ViewController/Imprint/LicensesViewController/LicensesViewController+TableView.swift
26 ./ViewControllers/ViewController/Imprint/ImprintViewController/ImprintViewController.swift
16 ./ViewControllers/ViewController/Imprint/ImprintViewController/ImprintViewController+ButtonAction.swift
69 ./API/JSONReader.swift
45 ./API/Model/Category.swift
34 ./API/Model/CategoriesDataHolder.swift
46 ./AppDelegate.swift
18 ./Views/Cells/ShoppingMoreTableViewCell.swift
15 ./Views/Cells/ShoppingMessageCell.swift
22 ./Views/Cells/BaseCollectionViewCells/StirnratenCollectionViewCell.swift
16 ./Views/Cells/ThemeLabelTableViewCell.swift
24 ./Views/Cells/ShoppingTimboTableViewCell.swift
20 ./Views/Cells/CategoryWelcomeCollectionViewCell.swift
25 ./Views/Cells/CategoryCollectionViewCell.swift
21 ./Views/Cells/RandomCollectionViewCell.swift
36 ./Views/Cells/ShoppingTableViewCell.swift
15 ./Views/Cells/FinishRightWordTableViewCell.swift
20 ./Views/Cells/RandomWelcomeCollectionViewCell.swift
14 ./Views/Cells/FinishWrongWordTableViewCell.swift
14 ./Views/Cells/ShoppingMessageTableViewCell.swift
14 ./Views/Cells/ImpressumButtonCollectionViewCell.swift
34 ./Views/ReusableView/RandomHeaderCollectionReusableView.swift
36 ./Views/ReusableView/CategoriesHeaderCollectionReusableView.swift
22 ./Views/Button/IconButton.swift
17 ./Views/Button/RoundButton.swift
55 ./Views/Button/LoadingButton.swift
39 ./Services/Notifications/OneSignalNotifcationExtension.swift
60 ./Services/Notifications/NotificationService.swift
48 ./Services/Notifications/OneSignalService.swift
17 ./Services/Analytics/AnalyticsDelegate.swift
48 ./Services/Analytics/MixpanelWrapper.swift
14 ./Services/Analytics/CustomerEvent.swift
36 ./Services/Analytics/AnalyticsTool.swift
50 ./Services/Analytics/TrackingEvent.swift
20 ./Internal Models/ShoppingElement.swift
20 ./Internal Models/UsedWord.swift
16 ./Internal Models/GuessedWords.swift
26 ./Internal Models/ShoppingItem.swift
16 ./Internal Models/New Group/ThirdParty.swift
15 ./Internal Models/New Group/ThirdpartyLicense.swift
17 ./Internal Models/CategoryHolder.swift
4954 total
```


## Unbenutzer Code
