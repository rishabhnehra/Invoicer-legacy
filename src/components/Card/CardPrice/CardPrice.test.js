import renderer from 'react-test-renderer';
import { CardPrice } from './CardPrice';

describe("<CardPrice />", () => {
    it("snapshot check", () => {
        const tree = renderer.create(<CardPrice description='Description' itemType='Item type' quantity={2} price={99900} />).toJSON();
        expect(tree).toMatchSnapshot();
    });
});