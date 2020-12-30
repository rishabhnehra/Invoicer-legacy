import renderer from 'react-test-renderer';
import { SimpleCard } from './SimpleCard';

describe("<SimpleCard />", () => {
    it("snapshot check", () => {
        const tree = renderer.create(<SimpleCard 
            header='Create Bill'  
            description={`This will initiate the flow of bill creation where
            you\'ll enter the required information and share
            it with your clients either by mail, WhatsApp or
            simple PDF`}
            actionLink='#'
            actionLabel='Click to get started'
        />).toJSON();
        expect(tree).toMatchSnapshot();
    });
});