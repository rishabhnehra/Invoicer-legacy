import renderer from 'react-test-renderer';
import { BusinessCard } from "./BusinessCard";

describe("<BusinessCard />", () => {
    it("snapshot check", () => {
        const tree = renderer.create(<BusinessCard 
            isSender={true}
            name='Rishabh Controls'
            gst= '24ABNPN1124A1ZA'
            address= {`Address #1
            Address #2`}
            phone={1234567890}
        />).toJSON();
        expect(tree).toMatchSnapshot();
    });
});