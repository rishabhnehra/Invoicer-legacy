import renderer from 'react-test-renderer';
import { BlankCard } from './BlankCard';

describe("<BlankCard />", () => {
    it("snapshot check", () => {
        const tree = renderer.create(<BlankCard>
            <h1>Any</h1>
            <p>element</p>
        </BlankCard>).toJSON();
        expect(tree).toMatchSnapshot();
    });
});