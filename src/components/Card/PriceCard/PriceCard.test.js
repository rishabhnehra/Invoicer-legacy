import renderer from 'react-test-renderer';
import { PriceCard } from './PriceCard';

describe("<PriceCard />", () => {
    it("snapshot check", () => {
        const tree = renderer.create(<PriceCard description='Description' itemType='Item type' quantity={2} price={99900} />).toJSON();
        expect(tree).toMatchSnapshot();
    });
});