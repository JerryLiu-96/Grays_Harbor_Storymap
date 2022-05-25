var config = {
    style: 'mapbox://styles/branigan/cjz37rcb003ib1cr3s8rnkt2d',
    accessToken: 'pk.eyJ1IjoibWJ4c29sdXRpb25zIiwiYSI6ImNrMm01aG9hdTBlZGwzbXQ1ZXVrNHNmejAifQ.QHQA0N6XPWddCXtvoODHZg',
    showMarkers: true,
    theme: 'dark',
    use3dTerrain: false,
    //title: 'Glaciers of Glacier National Park',
    //subtitle: 'Change in coverage from 1998 to 2015',
    //byline: '',
    //footer: 'Source: Story text from Wikipedia, August 2019. Data from <a href="https://www.usgs.gov/centers/norock/science/retreat-glaciers-glacier-national-park">USGS</a>',
    chapters: [
        {id: 'marina',
        alignment: 'left',
        title: 'Marina District',
        image: '',
        description: "Westport Marina is the largest coastal marina in the Pacific Northwest and home to Washington State's largest charter fishing fleet.",
        location: {
            center: [-124.113260, 46.907524],
            zoom: 13,
            pitch: 0.00,
            bearing: 0.00
        },
        onChapterEnter: [
            {
                layer:'',
                opacity: 0.25

        }],
        onChapterExit:[
            {

            }
        ]
    },

    {
        id: 'school',
        alignment: 'left',
        title: 'Marina District',
        image:'',
        description:"In 2015, the Ocosta School District became the first in United States to build a publicly funded vertical tsunami shelter, located at Ocosta Elementary School .",
        location: {
            center: [-124.100888, 46.863106],
            zoom: 13,
            pitch: 0.00,
            bearing: 0.00
        },
        onChapterEnter:[],
        onChapterExit:[]

    },

    {id: 'jetty',
    alignment:'left',
    title:'Westport Jetty',
    image:'',
    description:'Westport Jetty was built in 1902. It is believed that the Jetty changed current and reclaimed the land from the sea.',
    location: {
        center: [-124.138217, 46.905534],
        zoom: 13,
        pitch: 0.00,
        bearing: 0.00
    },
    onChapterEnter:[],
    onChapterExit:[]

    },

    {id:'condominum',
    alignment:'left',
    title:'Westport by the Sea Condominiums',
    image:'',
    description:'A fantastic condominium enjoying superb sea view, not far from lighthouse, now facing significant threat from coastal erosion',
    location: {
        center: [-124.126931, 46.886349],
        zoom: 13,
        pitch: 0.00,
        bearing: 0.00
    },
    onChapterEnter:[],
    onChapterExit:[]


},
{id:'light',
    alignment:'left',
    title:'Grays Harbor Lighthouse',
    image:'',
    description:'It marked the entrance to Grays Harbor and was first lit up in 1898. It was located only 400 feet from the shore when completed.',
    location: {
        center: [-124.116932, 46.887758],
        zoom: 13,
        pitch: 0.00,
        bearing: 0.00
    },
    onChapterEnter:[],
    onChapterExit:[]


},
{id:'downtown',
alignment:'left',
title:'Downtown Westport',
image:'',
description:'Downtown is mainly zoned for commercial and residential land use. One major concern for Downtown Westport is the rising sea may inundate the downtown in the future.',
location: {
    center: [-124.109605, 46.892591],
    zoom: 13,
    pitch: 0.00,
    bearing: 0.00
    },
    onChapterEnter:[],
    onChapterExit:[]


}
    ]
};