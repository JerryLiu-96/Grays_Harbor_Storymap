var config = {
    style: 'mapbox://styles/mapbox/light-v11',
    accessToken: 'pk.eyJ1IjoiemxpdTk2IiwiYSI6ImNsMnI3ZWNkcDA0bmwzYnFzcmxnbG9rejMifQ.KS1NO7CgxL3hJi94lTgidQ',
    showMarkers: false,
    theme: 'light',
    title: '',
    subtitle: '',
    byline: '',
    footer: '',
    chapters: [
        {
            id: 'shore-change',
            alignment: 'left',
            title: 'Visualizing Holocene Shoreline since 1700',
            range: '1700',
            image: '',
            description: 'Getting around Philadelphia on two wheels is fast, fun, and cheap. As a typical East Coast large city, the urban core is dense, so there is a lot within reach of a 15 minute ride... even mountain bike trails. Paired with the public transit infrastructure, cycling can be more efficient and much less expensive than driving (and parking) a car.',
            location: {
                center: [-124.0572, 46.8159],
                zoom: 10.5,
                pitch: 0.00,
                bearing: 0.00
            },
            record_yrs: [1700, 1860, 1911, 1926, 1942, 1954, 1967, 1974, 1986, 1995, 1997, 1999, 2001, 2006, 2015],
            // onChapterEnter: [
            //     {
            //         layer: 'phl-city-limits',
            //         opacity: .45
            //     }
            // ],
            // onChapterExit: [
            //     {
            //         layer: 'phl-city-limits',
            //         opacity: 0
            //     }
            // ]
        },
        {
            id: 'sea-level-rise',
            alignment: 'left',
            title: 'Sea Level Rise Projections',
            image: '',
            description: 'Philadelphia has XX miles of bike lanes, XX miles of which are protected. Drivers are getting more used to sharing the road, but ride defensively.',
            location: {
                center: [-124.0572, 46.8159],
                zoom: 10.5,
                pitch: 0.00,
                bearing: 0.00
            },

            lines: [
                {
                  name: 'RCP 8.5',
                  values: [{ year: 2020, ft: 0.1, lower: -0.1, upper:0.2 }, { year: 2030, ft: 0.2, lower:0, upper: 0.3}, { year: 2040, ft: 0.3, lower:0, upper: 0.6}, { year: 2050, ft: 0.4, lower:0, upper:0.8 }, { year: 2060, ft: 0.6, lower:0.1, upper:1.1 }, { year: 2070, ft: 0.8, lower:0.2, upper:1.5 },{ year: 2080, ft: 1.0, lower:0.3, upper:1.9 },{ year: 2090, ft: 1.2, lower:0.4, upper:2.4 },{ year: 2100, ft: 1.5, lower:0.5, upper:3.0 },{ year: 2110, ft: 1.6, lower:0.5, upper:3.2 },{ year: 2120, ft: 1.9, lower:0.7, upper:3.9 },{ year: 2130, ft: 2.1, lower:0.7, upper:4.5 },{ year: 2140, ft: 2.4, lower:0.8, upper:5.1 },{ year: 2150, ft: 2.7, lower:0.8, upper:5.8 }],
                  color: 'blue'
                },
                {
                  name: 'RCP 4.5',
                  values: [{ year: 2020, ft: 0.1, lower:-0.1, upper:0.2 }, { year: 2030, ft: 0.2, lower:0, upper:0.4 }, { year: 2040, ft: 0.3, lower:0, upper:0.5 }, { year: 2050, ft: 0.4, lower:0, upper:0.8 }, { year: 2060, ft: 0.5, lower:0, upper:1.0 }, { year: 2070, ft: 0.6, lower:0.1, upper:1.3 },{ year: 2080, ft: 0.8, lower:0.1, upper:1.6 },{ year: 2090, ft: 0.9, lower:0.1, upper:2.0 },{ year: 2100, ft: 1.1, lower:0.1, upper:2.4 },{ year: 2110, ft: 1.2, lower:0.1, upper:2.7 },{ year: 2120, ft: 1.3, lower:0.1, upper:3.1 },{ year: 2130, ft: 1.5, lower:0.1, upper:3.6 },{ year: 2140, ft: 1.6, lower:0, upper:4.1 },{ year: 2150, ft: 1.7, lower:-0.1, upper: 4.6}],
                  color: 'red'
                },

              ]
            // onChapterEnter: [
            //     {
            //         layer: 'phl-bike-network',
            //         opacity: 1
            //     }
            // ],
            // onChapterExit: []
        },
        {
            id: 'tsunami',
            alignment: 'left',
            title: 'A Possible Tsunami Scenario',
            image: '',
            description: 'Indego has been operating in Philadelphia since 20XX. The system initally was focused on Center City, but has expanded service to neighboring areas to support equitable mobility options to the city\'s residents.',
            location: {
                center: [-124.0572, 46.8159],
                zoom: 11,
                pitch: 0.00,
                bearing: 0.00
            },
            onChapterEnter: [
                {
                    layer: 'indego-stations',
                    opacity: 0.8
                }
            ],
            onChapterExit: [
                {
                    layer: 'indego-stations',
                    opacity: 0
                }
            ]
        },
        {
            id: 'belmont',
            alignment: 'left',
            title: 'Belmont Plateau Trails',
            image: '',
            description: 'A short ride along the Schuylkill River Trail from the Art Museum, Belmont is a twisty, log-ridden rollercoaster of a trail network. It is easy to get turned around, the underbrush is at times impenetrable, and short steep sections come out of nowhere. In other words, it\'s really fun',
            location: {
                center: [-75.20325, 39.99574],
                zoom: 14.99,
                pitch: 44.00,
                bearing: -40.00
            },
            onChapterEnter: [
                {
                    layer: 'belmont',
                    opacity: 1
                }
            ],
            onChapterExit: [
                {
                    layer: 'belmont',
                    opacity: 0
                }
            ]
        },
        {
            id: 'wiss',
            alignment: 'left',
            title: 'Wissahickon Park Trails',
            image: '',
            description: 'This steep, rocky gorge can be surprisingly technical. Follow the orange and yellow trails to repeatedly climb and descend through the schist hillsides (careful of the cliffs), or stick to the gravel Forbidden Drive for a relaxing ride along the creek. You\'ll forget you\'re in a city.',
            location: {
                center: [-75.21223, 40.05028],
                zoom: 13.08,
                pitch: 47.50,
                bearing: 32.80
            },
            onChapterEnter: [
                {
                    layer: 'wissahickon',
                    opacity: 1
                }
            ],
            onChapterExit: [
                {
                    layer: 'wissahickon',
                    opacity: 0
                }
            ]
        },
        {
            id: 'pennypack',
            alignment: 'left',
            title: 'Pennypack Park Trails',
            image: '',
            description: 'Pennypack is a great introduction trail system. Not too steep and not too technical, the beautiful wooded park also provides a great escape from urban life. The south side trails are originally bridle trails, so be nice to equestrians and dismount when you approach them.',
            location: {
                center: [-75.05685, 40.06839],
                zoom: 13.73,
                pitch: 43.50,
                bearing: 96.80
            },
            onChapterEnter: [
                {
                    layer: 'pennypack',
                    opacity: 1
                }
            ],
            onChapterExit: [
                {
                    layer: 'pennypack',
                    opacity: 0
                }
            ]
        }
    ]
};
