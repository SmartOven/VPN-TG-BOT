import os

src_path = str(os.path.join(os.path.dirname(__file__), "..", "..", "connection_guides_screenshots/"))
android_path = src_path + "android/"
ios_path = src_path + "ios/"
windows_path = src_path + "windows/"

windows_guide_photos = [
    [
        # Step 1
        windows_path + "1_1.png",
        windows_path + "1_2.png"

        # "AgACAgIAAx0CaVbYGQADn2Jep0E0-ZY-SC7NpnrXz4OjY87uAAJCuDEbFGj4Sv7nlbfpxN8uAQADAgADeAADJAQ",
        # "AgACAgIAAx0CaVbYGQADoWJep0MOaj6ZbWKnW8uDE7GkJ3WgAAJDuDEbFGj4SmRZSL1c0nQfAQADAgADeQADJAQ"
    ],
    [
        # Step 2
        windows_path + "2_1.png",
        windows_path + "2_2.png"

        # "AgACAgIAAx0CaVbYGQADo2Jep1Q8kKMEFl3TP2Hl0LKtH0N_AAJFuDEbFGj4SggoaA3ADQGOAQADAgADeAADJAQ",
        # "AgACAgIAAx0CaVbYGQADpWJep1fu-wRVSd1X6oYk-DHKSga_AAJGuDEbFGj4SrPtnGzAkNTgAQADAgADeQADJAQ"
    ],
    [
        # Step 3
        windows_path + "3_1.png",
        windows_path + "3_2.png",
        windows_path + "3_3.png",
        windows_path + "3_4.png"

        # "AgACAgIAAx0CaVbYGQADp2Jep23VmPkJugAB5N_suBkNL--j1AACR7gxGxRo-EqlHQSeoy7SAAEBAAMCAAN5AAMkBA",
        # "AgACAgIAAx0CaVbYGQADqWJep29IAS6ZGr3Omzur-IzfWuo3AAJIuDEbFGj4SmEuVa63JyYAAQEAAwIAA3gAAyQE",
        # "AgACAgIAAx0CaVbYGQADq2Jep3EycKxKLR3bmB242p92b7njAAJJuDEbFGj4St7riPXWzh8HAQADAgADeAADJAQ",
        # "AgACAgIAAx0CaVbYGQADrWJep3S4Wrv2uq7MmRzh182o0V5GAAJKuDEbFGj4SpuyvkwX4pe3AQADAgADeAADJAQ"
    ],
    [
        # Step 4
        windows_path + "4_1.png",
        windows_path + "4_2.png",
        windows_path + "4_3.png"

        # "AgACAgIAAx0CaVbYGQADr2Jep4xzrKuZa3atS9KCBI-07qJLAAJLuDEbFGj4Su8dq0vWCAE8AQADAgADeQADJAQ",
        # "AgACAgIAAx0CaVbYGQADsWJep5bZglHUZn2VWvJZbvSKJT4nAAJMuDEbFGj4SqLr9dCudSvXAQADAgADeQADJAQ",
        # "AgACAgIAAx0CaVbYGQADs2Jep6C74pSrXh5tpnss1jMoSsiFAAJNuDEbFGj4Sks2Z6UNv4dHAQADAgADeQADJAQ"
    ],
    [
        # Step 5
        windows_path + "5_1.png",
        windows_path + "5_2.png",
        windows_path + "5_3.png",
        windows_path + "5_4.png"

        # "AgACAgIAAx0CaVbYGQADtWJep675CsuTXGqvytrwoknnaRbLAAJOuDEbFGj4SjK2WYKN5Ri5AQADAgADeQADJAQ",
        # "AgACAgIAAx0CaVbYGQADt2Jep7D12joMzwFfTO-7zktX7VN-AAJPuDEbFGj4Shqa78kay854AQADAgADeQADJAQ",
        # "AgACAgIAAx0CaVbYGQADuWJep7OyN9a2Heqc4jHiMqcTpWMoAAJQuDEbFGj4Sm-UWLi342BfAQADAgADbQADJAQ",
        # "AgACAgIAAx0CaVbYGQADu2Jep7UdViUsUbJ7268ifELInvP4AAJRuDEbFGj4SkgiSPrXfxWrAQADAgADeAADJAQ"
    ],
    [
        # Step 6
        windows_path + "6_1.png",
        windows_path + "6_2.png",
        windows_path + "6_3.png"

        # "AgACAgIAAx0CaVbYGQADvWJep9Az9M__ZGNNNSMNmBeXh-udAAJSuDEbFGj4St-wi0XLbCgvAQADAgADeQADJAQ",
        # "AgACAgIAAx0CaVbYGQADv2Jep9PGJKe4HfEM98Tyy3AEzdDvAAJTuDEbFGj4SjFGZfLtz1f4AQADAgADeQADJAQ",
        # "AgACAgIAAx0CaVbYGQADwWJep9ZtgFsja7twsZmrgz-6Sy4eAAJUuDEbFGj4SmeiLtFm8bwTAQADAgADeAADJAQ"
    ],
    [
        # Step 7
        windows_path + "7_1.png",
        windows_path + "7_2.png",
        windows_path + "7_3.png"

        # "AgACAgIAAx0CaVbYGQADw2JeqCE-YBxvTKQT0VuVsD1tdxKoAAJWuDEbFGj4SsprhyrzM-CTAQADAgADeQADJAQ",
        # "AgACAgIAAx0CaVbYGQADxWJeqCPFXw5C60U8NjjMQl6u5YdMAAJXuDEbFGj4Suke1uSP-HfTAQADAgADeAADJAQ",
        # "AgACAgIAAx0CaVbYGQADx2JeqCWOOTpYEiTQMjgq8sdDGnypAAJYuDEbFGj4SqoLks83rGO1AQADAgADeQADJAQ"
    ],
    [
        # Step 8
        windows_path + "8_1.png"

        # "AgACAgIAAx0CaVbYGQADyWJeqCe8pRTO8jG9VEuNCfE81ChzAAJZuDEbFGj4Sl9qIdUji4BVAQADAgADeAADJAQ"
    ],
]

android_guide_photos = [
    [
        # Step 1
        android_path + "1_1.png"

        # "AgACAgIAAx0CaVbYGQADg2JephoItNoo7fStHfjcB6LRfWLgAAIzuDEbFGj4Sipj0vBhNKGPAQADAgADeQADJAQ"
    ],
    [
        # Step 2
        android_path + "2_1.png",
        android_path + "2_2.png"

        # "AgACAgIAAx0CaVbYGQADhWJepilMP8f6PMDl1RvoovvE-FW5AAI0uDEbFGj4SjkJyM4MQMxnAQADAgADeQADJAQ",
        # "AgACAgIAAx0CaVbYGQADh2JepqQldlOW164kdk8c_iYpvmcTAAI2uDEbFGj4Sl6cPf0bdVCtAQADAgADeQADJAQ"
    ],
    [
        # Step 3
        android_path + "3_1.png"

        # "AgACAgIAAx0CaVbYGQADiWJeprNGM5Gkg4RRN4M6obu7DlYRAAI3uDEbFGj4SvisB9KR4-gAAQEAAwIAA3kAAyQE"
    ],
    [
        # Step 4
        android_path + "4_1.png"

        # "AgACAgIAAx0CaVbYGQADi2Jepr1vtZ0GGHQrJLwO6IEpOhRvAAI4uDEbFGj4Svceicv5CVgIAQADAgADeQADJAQ"
    ],
    [
        # Step 5
        android_path + "5_1.png",
        android_path + "5_2.png",
        android_path + "5_3.png"

        # "AgACAgIAAx0CaVbYGQADjWJepsvmDyag0szCNMzsA-D36lhqAAI6uDEbFGj4Sn8EsfBF7DyEAQADAgADeQADJAQ",
        # "AgACAgIAAx0CaVbYGQADj2Jeps0ByQFZvP2kEjVDBGz1XNQBAAI7uDEbFGj4Sj2Luu6A5FHnAQADAgADeQADJAQ",
        # "AgACAgIAAx0CaVbYGQADk2Jepur1z0pyOTViBhmKg0Q9lb_RAAI8uDEbFGj4Sox4iwQHeErBAQADAgADeQADJAQ"
    ],
    [
        # Step 6
        android_path + "6_1.png",
        android_path + "6_2.png",
        android_path + "6_3.png",
        android_path + "6_4.png",
        android_path + "6_5.png"

        # "AgACAgIAAx0CaVbYGQADlWJepwXklqzTOkydxWmNIMKRYVoeAAI9uDEbFGj4Ss4ewlXXGvUJAQADAgADeQADJAQ",
        # "AgACAgIAAx0CaVbYGQADl2Jepwcs640ZbtYLKSZQjwZwqXQ6AAI-uDEbFGj4SkCmffovm-rjAQADAgADeQADJAQ",
        # "AgACAgIAAx0CaVbYGQADmWJepwnZ_Us2OjnsMpPrD8tMr-_NAAI_uDEbFGj4SrV9ni-DVcpuAQADAgADeQADJAQ",
        # "AgACAgIAAx0CaVbYGQADm2JepwukRchu-9_vj6nRrMu1o4iYAAJAuDEbFGj4SqBtMESWSkBrAQADAgADeQADJAQ",
        # "AgACAgIAAx0CaVbYGQADnWJepw1VwGlCLQnJHkl2EyXRpRTFAAJBuDEbFGj4SrES7jVYDqNEAQADAgADeQADJAQ"
    ]
]

ios_guide_photos = [
    [
        # Step 1
        ios_path + "1_1.png",
        ios_path + "1_2.png"

        # "AgACAgIAAx0CaVbYGQADaGJepJ0_49RXTm3TEJP118jtrZgHAAIYuDEbFGj4Sg9-nyfPaexbAQADAgADeQADJAQ",
        # "AgACAgIAAx0CaVbYGQADamJepKRcx7E6VdyN1hDxTTpBpoLGAAIZuDEbFGj4Sq7kkrZay8wPAQADAgADeQADJAQ"
    ],
    [
        # Step 2
        ios_path + "2_1.png",
        ios_path + "2_2.png"

        # "AgACAgIAAx0CaVbYGQADb2JepSZhbWZ072Be6S099-Bz59uZAAIauDEbFGj4Skv9HgUAARZW0AEAAwIAA3kAAyQE",
        # "AgACAgIAAx0CaVbYGQADcWJepSgv3LJ6QFZCivkXDO27RqdXAAIbuDEbFGj4Sr71QBU-C5jfAQADAgADeQADJAQ"
    ],
    [
        # Step 3
        ios_path + "3_1.png",
        ios_path + "3_2.png",
        ios_path + "3_3.png",
        ios_path + "3_4.png"

        # "AgACAgIAAx0CaVbYGQADc2JepaxU4RoMk1W4NpBp4HJT8DUwAAIcuDEbFGj4Sn53SJQgYE6hAQADAgADeQADJAQ",
        # "AgACAgIAAx0CaVbYGQADdWJepa486XZPRepsB8QUWBNuthRDAAIduDEbFGj4SliGYkpBtYWeAQADAgADeQADJAQ",
        # "AgACAgIAAx0CaVbYGQADd2JepbAPatc0B8hg1Ra-5n59UXa0AAIeuDEbFGj4SqmbKWy4wdWIAQADAgADeQADJAQ",
        # "AgACAgIAAx0CaVbYGQADeWJepbP3WJF67rmdx6kC1UHqW0L9AAIfuDEbFGj4SlPpOS5doSNxAQADAgADeQADJAQ"
    ],
    [
        # Step 4
        ios_path + "4_1.png",
        ios_path + "4_2.png",
        ios_path + "4_3.png",
        ios_path + "4_4.png"

        # "AgACAgIAAx0CaVbYGQADe2Jepdb0_bSC4_T02RyhxLAQH357AAIguDEbFGj4SlovhWOnUwi4AQADAgADeQADJAQ",
        # "AgACAgIAAx0CaVbYGQADfWJepdmF9hE81sJ8rNxg-sxtsMRnAAIhuDEbFGj4SlXFZE5KW2fYAQADAgADeQADJAQ",
        # "AgACAgIAAx0CaVbYGQADf2JepdsxsO2hVqcZlGiYrYFOwBM3AAIiuDEbFGj4Sl9Aa6NSqbfQAQADAgADeQADJAQ",
        # "AgACAgIAAx0CaVbYGQADgWJepd33oSCDJbBke8WANnqvEeCXAAIjuDEbFGj4SlPiqsGKDTQGAQADAgADeQADJAQ"
    ]
]
